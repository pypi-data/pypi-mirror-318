from computenestcli.service.project_setup.setup_handler import SetupHandler
from computenestcli.common import project_setup_constant

# 从源代码使用buildpacks构建容器镜像并创建服务
class BuildpacksSetupHandler(SetupHandler):

    def validate_parameters(self):
        pass

    def generate_templates(self):
        self.select_package()
        self._replace_variables()
        self.generate_specified_templates(project_setup_constant.INPUT_BUILDPACKS_ROS_TEMPLATE_NAME,
                                          project_setup_constant.INPUT_ECS_IMAGE_CONFIG_NAME)

    def _replace_variables(self):
        custom_parameters = self.parameters.get(project_setup_constant.CUSTOM_PARAMETERS_KEY)
        docker_run_env_parameters = self._build_docker_run_parameters(custom_parameters)
        if docker_run_env_parameters and len(docker_run_env_parameters) > 0:
            self.parameters[project_setup_constant.DOCKER_RUN_ENV_ARGS] = docker_run_env_parameters
        self.parameters[project_setup_constant.ECS_IMAGE_BUILDER_COMMAND_CONTENT_KEY] = \
            self._generate_ecs_image_builder_command()

    def _build_docker_run_parameters(self, custom_parameters: list):
        if not custom_parameters:
            return None
        run_parameters = []
        for param in custom_parameters:
            name = param.get("Name")
            if name:
                run_parameters.append(f"-e {name}=${{{name}}}")  # 拼接环境变量格式
            # 返回拼接的参数字符串
        return ' '.join(run_parameters)

    def _generate_ecs_image_builder_command(self):
        docker_image_name = self.parameters.get(project_setup_constant.REPO_NAME_KEY)
        self.parameters[project_setup_constant.DOCKER_IMAGE_NAME_KEY] = docker_image_name
        command = (
            'curl -L https://github.com/buildpacks/pack/releases/download/v0.35.1/pack-v0.35.1-linux.tgz -o pack.tgz\n'
            'tar xvf pack.tgz\n'
            './pack config default-builder gcr.io/buildpacks/builder\n'
            f'./pack build {docker_image_name}\n'
            'rm pack.tgz pack\n'
            "docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}'"
            f" | grep -v '^{docker_image_name}:'"
            " | awk '{print $2}' | xargs docker rmi"
        )
        return command