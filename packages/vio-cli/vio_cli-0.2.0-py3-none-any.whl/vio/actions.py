import logging
import os
import subprocess

from vio.clients import VioAPIClient, VioS3Client
from vio.exceptions import ImproperlyConfigured
from vio.utils import decode_template, encode_file, encode_templates_to_dict, write_to_file

logger = logging.getLogger(__name__)


class Action:
    def __init__(
        self,
        theme: str,
        api_key=None,
    ):
        self.theme = theme
        self.api_key = api_key if api_key else self.get_api_key()
        self.api_client = self.get_api_client()
    
    def get_api_client(self):
        client = VioAPIClient(self.api_key)
        return client

    def get_api_key(self):
        api_key = os.getenv("VIO_API_KEY")
        if not api_key:
            raise ImproperlyConfigured(
                "The VIO_API_KEY environment variable must be set."
            )
        return api_key


class DeploymentAction(Action):
    def __init__(
        self,
        theme: str,
        template_dir=None,
        static_dir=None,
        custom_css=None,
        custom_js=None,
        api_key=None,
        version=None,
        *args,
        **kwargs,
    ):
        super().__init__(theme, api_key=api_key)
        self.template_dir = template_dir
        self.static_dir = static_dir
        self.custom_css = custom_css
        self.custom_js = custom_js
        self.version = version if version else self.get_version()

    def run(self):
        encoded_templates = []

        if self.static_dir:
            credentials = self.api_client.get_credentials(self.theme)
            s3_client = VioS3Client(
                credentials["s3_access_key_id"],
                credentials["s3_secret_access_key"],
                credentials["s3_prefix"],
                credentials["s3_bucket"],
            )
            s3_client.sync(self.theme, self.static_dir)
            logger.info("Successfully updated static files")

        if self.template_dir:
            encoded_templates = encode_templates_to_dict(self.template_dir)

        self.api_client.update_themes(self.theme, encoded_templates, self.version)
        logger.info("Successfully updated templates")

        if self.custom_css or self.custom_js:
            settings = {}
            if self.custom_css:
                settings["custom_css"] = encode_file(self.custom_css)
            if self.custom_js:
                settings["custom_js"] = encode_file(self.custom_js)
            self.api_client.update_settings(self.theme, settings)
            logger.info("Successfully updated settings")

        logger.info(f"Deployment finished (version {self.version})")

    def get_s3_client(self):
        client = VioS3Client()
        return client

    def get_version(self):
        process = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"],
            shell=False,
            stdout=subprocess.PIPE,
        )
        git_short_hash = process.communicate()[0].strip()
        version = git_short_hash.decode()
        return version


class DownloadTemplatesAction(Action):
    def __init__(
        self,
        theme: str,
        template_dir=None,
        api_key=None,
        *args,
        **kwargs,
    ):
        super().__init__(theme, api_key=api_key)
        self.template_dir = template_dir

    def run(self):
        theme = self.api_client.get_theme(self.theme)
        for template_name, encoded_template in theme["templates"].items():
            filename = self.template_dir + "/" + self.theme + "/" + template_name
            decoded_template = decode_template(encoded_template)
            write_to_file(filename, decoded_template)
        logger.info("Successfully downloaded templates")
