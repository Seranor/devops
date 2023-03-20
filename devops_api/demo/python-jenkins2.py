import jenkins


class Jenkinsapi(object):
    def __init__(self, url, user, token):
        self.server_url = url
        self.user = user
        self.token = token
        self.conn = jenkins.Jenkins(self.server_url, username=self.user, password=self.token)

    def get_jobs(self):
        """
        获取所有的构建项目列表
        :return:
        """
        return self.conn.get_jobs()

    def get_views(self):
        """
        获取所有的构建视图
        :return:
        """

    def get_job_info(self, job):
        """
        根据项目名获取构建项目
        :param job:
        :return:
        """
        return self.conn.get_job_info(job)

    def build_job(self, job, **kwargs):
        """
        开始构建项目
        :param job:
        :param kwargs:
        :return:
        """
        # dict1 = {"version":11} # 参数话构建
        # dict2 = {'Status': 'Rollback', 'BUILD_ID': '26'} # 回滚
        return self.conn.build_job(job, parameters=kwargs)

    def get_build_info(self, job, build_number):
        """
        通过构建编号获取构建项目的构建记录
        :param job:
        :param build_number:
        :return:
        """
        return self.conn.get_build_info(job, build_number)

    def get_job_config(self, job):
        '''
        获取xml文件
        '''
        res = self.conn.get_job_config(job)
        print(res)

    def create_job(self, name, config_xml):
        '''
        任务名字
        xml格式的字符串
        '''
        self.conn.create_job(name, config_xml)

    def update_job(self, name, config_xml):
        res = self.conn.reconfig_job(name, config_xml)
        print(res)


if __name__ == '__main__':
    server_url = 'http://192.168.150.21:8080/'
    username = 'admin'
    password = '119f34391f13b9de5ab6a6976cbfa42881'
    server = Jenkinsapi(server_url, username, password)

    jobs = server.get_jobs()
    print(jobs)

    # views = server.get_views()
    # print(views)
    # job = server.get_job_info("project-1")
    # print(job)

    # build_number = server.build_job("project-1")
    # print(build_number)

    # info = server.get_build_info("project-1", 2)
    # print(info)

    # 先获取已有构建项目的配置文档
    config_xml = server.get_job_config("ruoyi-dev-gateway")
    print(config_xml)

    config_xml = """
  <properties>
    <com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty plugin="gitlab-plugin@1.6.0">
      <gitLabConnection></gitLabConnection>
      <jobCredentialId></jobCredentialId>
      <useAlternativeCredential>false</useAlternativeCredential>
    </com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
        <hudson.model.StringParameterDefinition>
          <name>srcUrl</name>
          <defaultValue>http://192.168.150.22:8076/gitlab-instance-1c74674d/ruoyi.git</defaultValue>
          <trim>true</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.ChoiceParameterDefinition>
          <name>buildTools</name>
          <choices class="java.util.Arrays$ArrayList">
            <a class="string-array">
              <string>maven</string>
              <string>gradle</string>
            </a>
          </choices>
        </hudson.model.ChoiceParameterDefinition>
        <net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition plugin="git-parameter@0.9.18">
          <name>branchName</name>
          <uuid>bd7fe096-569c-4924-b35c-02f51b8571f6</uuid>
          <type>PT_BRANCH</type>
          <branch></branch>
          <tagFilter>*</tagFilter>
          <branchFilter>.*</branchFilter>
          <sortMode>NONE</sortMode>
          <defaultValue>main</defaultValue>
          <selectedValue>NONE</selectedValue>
          <useRepository>http://192.168.150.22:8076/gitlab-instance-1c74674d/ruoyi.git</useRepository>
          <quickFilterEnabled>false</quickFilterEnabled>
          <listSize>5</listSize>
          <requiredParameter>false</requiredParameter>
        </net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition>
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
  </properties>
    """
    server.create_job("project-2", config_xml=config_xml)
