##Jenkins Plugins Repo API

from urllib.request import Request, urlopen
import re

class JenkinsPlugins:
	#Final Variables
	JenkinsPluginsEndpoint = "https://updates.jenkins-ci.org/download/plugins/"
	JenkinsPluginsFileExtenion = ".hpi"
	
	#Returns Plugins List
	def list(self):
		jenkinsPluginsRequest = Request(self.JenkinsPluginsEndpoint, headers={'User-Agent': 'Mozilla/5.0'})
		jenkinsPluginsHTMLData = urlopen(jenkinsPluginsRequest).read().decode("utf-8")
		return [plugin[:-1] for plugin in re.findall("<a.*?>(.+?)</a>", jenkinsPluginsHTMLData)[5:]]
		
	#Returns Plugin Versions List
	def listVersions(self, pluginName):
		jenkinsPluginsVersionsRequest = Request(self.JenkinsPluginsEndpoint+"/"+pluginName, headers={'User-Agent': 'Mozilla/5.0'})
		jenkinsPluginsVersionsHTMLData = urlopen(jenkinsPluginsVersionsRequest).read().decode("utf-8")
		return [plugin for plugin in re.findall("<a.*?'>(.+?)</a>", jenkinsPluginsVersionsHTMLData)[1:]]
	
	#Downloads Latest Version Of Plugin	
	def getVersion(self, pluginName, version):	
		jenkinsPluginsVersionsRequest = Request(self.JenkinsPluginsEndpoint+"/"+pluginName+"/"+version+"/"+pluginName+self.JenkinsPluginsFileExtenion, headers={'User-Agent': 'Mozilla/5.0'})
		return urlopen(jenkinsPluginsVersionsRequest).read()
		
JenkinsPlugins = JenkinsPlugins()
#print(JenkinsPlugins.list())
#print(JenkinsPlugins.listVersions("bootstrap"))
print(JenkinsPlugins.getVersion("bootstrap","1.0"))