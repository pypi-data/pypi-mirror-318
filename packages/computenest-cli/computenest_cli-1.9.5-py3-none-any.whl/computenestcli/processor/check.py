import yaml
import os
from computenestcli.common import constant
from computenestcli.base_log import get_user_logger

user_logger = get_user_logger()


class CheckProcessor:
    def __init__(self, config, file_path, service_name, service_id):
        self.config = config
        self.file_path = file_path
        self.service_name = service_name
        self.service_id = service_id
        self.checks = [self.validate_service_name_and_id, self.validate_allowed_regions, self.validate_image_key]
        self.errors = []

    def validate_service_name_and_id(self):
        service_config = self.config[constant.SERVICE]

        # 检查输入参数
        if not self.service_name and not self.service_id:
            service_info_list = service_config.get(constant.SERVICE_INFO)
            if isinstance(service_info_list, dict):
                service_info_list = [service_info_list]
            if not service_info_list or len(service_info_list) == 0:
                self.errors.append("service_id or service_name should provided.")
                user_logger.log('service_id or service_name should provided.')
                return False
            for service_info in service_info_list:
                if not service_info.get(constant.NAME):
                    self.errors.append("service_id or service_name should provided.")
                    return False
        return True

    def validate_allowed_regions(self):
        support_regions = []
        if constant.ARTIFACT not in self.config:
            return True
        deploy_metadata = self.config[constant.SERVICE][constant.DEPLOY_METADATA]
        if self.config[constant.SERVICE][constant.SERVICE_TYPE] == constant.MANAGED:
            template_configs = deploy_metadata[constant.SUPPLIER_DEPLOY_METADATA][constant.SUPPLIER_TEMPLATE_CONFIGS]
        else:
            template_configs = deploy_metadata[constant.TEMPLATE_CONFIGS]

        for artifact in self.config[constant.ARTIFACT]:
            if self.config[constant.ARTIFACT][artifact][constant.ARTIFACT_TYPE] == constant.ECS_IMAGE:
                support_region_ids = self.config[constant.ARTIFACT][artifact].get(constant.SUPPORT_REGION_IDS, "")

                if support_region_ids:
                    support_regions.extend(support_region_ids)
                    for config in template_configs:
                        allowed_regions = config[constant.ALLOWED_REGIONS]
                        if set(allowed_regions).issubset(set(support_regions)):
                            continue
                        else:
                            self.errors.append(
                                "The AllowedRegions in TemplateConfigs are beyond the scope of SupportRegionIds in Artifact.")
                            return False
        return True

    def validate_image_key(self):
        deploy_metadata = self.config[constant.SERVICE][constant.DEPLOY_METADATA]

        if self.config[constant.SERVICE][constant.SERVICE_TYPE] == constant.MANAGED:
            template_configs = deploy_metadata[constant.SUPPLIER_DEPLOY_METADATA][constant.SUPPLIER_TEMPLATE_CONFIGS]
        else:
            template_configs = deploy_metadata[constant.TEMPLATE_CONFIGS]

        template_image_ids = set()
        config_image_ids = set()
        for template in template_configs:
            # 将相对路径替换成绝对路径
            template_path = os.path.join(os.path.dirname(self.file_path), template.get(constant.URL))
            template = self.read_yaml_file(template_path)
            template_image_ids.update(self.get_image_ids(template))
            supplier_deploy_metadata = deploy_metadata.get(constant.SUPPLIER_DEPLOY_METADATA, None)
            if supplier_deploy_metadata is None:
                return True
            if constant.ARTIFACT_RELATION not in supplier_deploy_metadata:
                return True
            config_image_ids.update(self.config[constant.SERVICE][constant.DEPLOY_METADATA][
                                        constant.SUPPLIER_DEPLOY_METADATA][constant.ARTIFACT_RELATION].keys())
        if not config_image_ids.issubset(template_image_ids):
            self.errors.append("The ImageId in template.yaml does not match the image identifier in config.yaml.")
            return False

        return True

    @staticmethod
    def read_yaml_file(file):
        with open(file, 'r') as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_image_ids(template):
        image_ids = set()
        CheckProcessor.search_image_ids(template, image_ids)
        return image_ids

    @staticmethod
    def search_image_ids(obj, image_ids):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == constant.IMAGE_ID:
                    if isinstance(value, dict):
                        for inner_value in value.values():
                            if isinstance(inner_value, str):
                                image_ids.add(inner_value)
                    elif isinstance(value, str):
                        image_ids.add(value)
                else:
                    CheckProcessor.search_image_ids(value, image_ids)
        elif isinstance(obj, list):
            for item in obj:
                CheckProcessor.search_image_ids(item, image_ids)
        return image_ids

    def run_checks(self):
        for check_func in self.checks:
            if not check_func():
                return False
        return True

    def print_errors(self):
        if self.errors:
            error_messages = []
            for error in self.errors:
                error_messages.append(error)
            raise ValueError(
                f"YAML file parameters are incorrect. Please modify and try again.\nThe error messages: {', '.join(error_messages)}")
        else:
            user_logger.error("Config is valid.")

    def processor(self):
        if self.run_checks():
            user_logger.info("Validation check: The config.yaml is correct!")
        else:
            self.print_errors()
