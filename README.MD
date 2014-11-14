<h2>HelpZY 使用指南</h2>

<p>You can just read <a href="#quickstart">Quick Start</a>.</p>

<hr />

<h2>1.获取源码</h2>

<p>项目源代码托管在Github上.请从链接 <strong><a href="https://github.com/greyyang/helpzy">HelpZY</a></strong> 下载.
也可以通过Git下载分支: <strong>git@github.com:greyyang/helpzy.git</strong></p>

<hr />

<h2>2.安装</h2>

<p>项目运行所需要的文件在项目中的required文件夹内</p>

<blockquote>
  <ul>
  <li>python-3.4.2.msi</li>
  <li>pywin32-219.win32-py3.4.exe</li>
  <li>xlrd-0.9.3</li>
  </ul>
</blockquote>

<p>请依次进行如下安装</p>

<h3>(1)python-3.4.2.msi</h3>

<p>请执行默认安装</p>

<h3>(2)pywin32-219.win32-py3.4.exe</h3>

<p>请执行默认安装</p>

<h3>(3)xlrd-0.9.3</h3>

<p>请将<strong>xlrd-0.9.3\xlrd</strong>文件夹拷贝到python安装路径下(默认是C:\Python34)的<strong>Lib\site-packages</strong>文件夹下.</p>

<hr />

<h2>3.配置</h2>

<p>项目的可配置文件如下:</p>

<blockquote>
  <ul>
  <li>conf.json 文件</li>
  <li>cmd文件夹中的命令文件</li>
  <li>configuration\cmdNames.json 文件</li>
  </ul>
</blockquote>

<h3>(1)conf.json文件</h3>

<p><code>json
{
    "cmdPath": "cmd", 
    "dataPath": "data", 
    "targetPath": "target",
    "targetName": "report",
    "tamplatePath":"tamplate\\ReportTamplate.xlsx",
    "cmdNameListPath":"configuration\\cmdNames.json"
}
</code></p>

<blockquote>
  <ul>
  <li><em>cmdPath:</em>          配置存放命令文件的<strong>文件夹路径</strong> (默认为cmd\*)</li>
  <li><em>dataPath:</em>         配置存放源数据的<strong>文件夹路径</strong> (默认为data\*)</li>
  <li><em>targetPath:</em>       配置存放到处报表文件的<strong>文件夹路径</strong> (默认为target文件夹下)</li>
  <li><em>tamplatePath:</em>     配置报表模板存放的<strong>文件路径</strong> (默认为tamplate\ReportTamplate.xlsx)</li>
  <li><em>cmdNameListPath:</em>  配置存放命令名和文件名的映射关系的<strong>文件路径</strong>(默认为configuration\cmdNames.json)</li>
  </ul>
</blockquote>

<h3>(2)cmd目录下的命令文件</h3>

<p><code>json
//(示例) MIFI统计操作
{
    "cmdType": "TMC",
    "headerName": "备注",
    "content": "批次:武汉高校MIFI活动, 档次:预存300送MIFI|批次:武汉高校MIFI活动, 档次:预存180送MIFI",
    "embedContent":"",
    "mutexHeader":"",
    "mutexContent":"",
    "targetY": "Y"
}
</code></p>

<h4><strong>cmdType:</strong></h4>

<p>该配置用于指定该文件用于执行何种命令.
现有的命令选择有:TMC(Total Match Count)和ECC(Embed Content Count)
<em>TMC</em> : 通过完全匹配文本计算总数.例如匹配受理类型一栏中出现了多少次"补卡".
<em>ECC</em> : 通过获取嵌入内容计算数据.例如通过"批次:积分兑换通用电子券（常态化）, 档次:100积分兑换1.5元通用电子券"把文本中的100数字或1.5数字取出进行计算.(暂时废弃)</p>

<h4><strong>headerName</strong>:</h4>

<p>需要统计的表头名字,例如"备注".</p>

<h4><strong>content</strong>:</h4>

<p>需要匹配的字符串.</p>

<h4><strong>embedContent</strong>:</h4>

<p>暂时废弃</p>

<h4><strong>mutexHeader</strong>:</h4>

<p>暂时废弃</p>

<h4><strong>metexContent</strong>:</h4>

<p>暂时废弃</p>

<h4><strong>targetY</strong>:</h4>

<p>需要在模板表中写入列位置,例如"Y"列</p>

<hr />

<h2 id="quickstart" name="quickstart">4.使用</h2>
