
<template>
<div class="mainpageblock">
<el-row :gutter="22">
		<el-breadcrumb separator-class="el-icon-arrow-right" style="font-size:20px;left:20px;position:absolute">
		  <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
		  <el-breadcrumb-item :to="{ path: '/dashboard' }">PostMapping()</el-breadcrumb-item>
		  <el-breadcrumb-item :to="{ path: '/case' }">Register</el-breadcrumb-item>
		  <el-breadcrumb-item>13101144/health-check</el-breadcrumb-item>
		</el-breadcrumb>
	<el-col :span="11">
		<div class="owncode" v-infinite-scroll="load">
				<pre  class="language-java line-numbers">
					<code>{{codepiece}}</code>
				</pre>
		</div>
		<div class="owncode" v-infinite-scroll="load">
				<div style="font-size:15px;">{{fileNameshow}}</div>
				<pre  class="language-java line-numbers">
					<code>{{codefile}}</code>
				</pre>
		</div>
	</el-col>
	<el-col :span="11">
		<div class="container">			
			<div class="chart" ><chart :option="option" :auto-resize="true" @click="changeConcept"></chart></div>
			
		</div>
		
		<div class='title'>跳转查看:</div>
					<div class="casecard">
			  <el-col :span="12" v-for="item in fileName" :index="item.index" :key="item.index">
				<el-card :body-style="{ padding: '10px' }" shadow="hover" style="background-color:#C0C4CC;marginLeft:10px;marginRight:10px;" @click.native="exchangecode(item.method)">
				  <div style="font-size:19px;padding: 14px;">
					<span>{{item.method}}</span>
				  </div>
				  <div style="font-size:15px;padding:10px;">
					<span>{{item.fileName}}</span>
				  </div>
				</el-card>
			 </el-col>
			</div>
			
	</el-col>
</el-row>	
</div>

</template>

<script>
import Prism from "prismjs";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);
export default {
	components: {
	 VChart
	 },
	provide: {
    [THEME_KEY]: "light",
	},
	data(){
			return {
			option: {
				title: {
				  text: "对象生成及方法调用",
				  left: "center",
				},
				tooltip: {
				  trigger: "item"
				},
				series: [
				  {
					name: "对象及方法调用",
					type: "graph",
					layout:'force',
					edgeSymbol:['','arrow'],
					label:{
					  show:true
					},
					force:{
					  repulsion:1000,
					  edgeLength: [100,200]
					},
					draggable:true,
					data: [
					  {
						name: "@RequestBody User user,SingleVariableDeclaration,24",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "user.getPassword(),MethodInvocation,25",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "bCryptPasswordEncoder.encode(user.getPassword()),MethodInvocation,25",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "user.setRole(\"ROLE_USER\"),MethodInvocation,26",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "new Date(),ClassInstanceCreation,27",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "user.setCreated(new Date()),MethodInvocation,27",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "userService.save(user),MethodInvocation,28",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "R.success(),MethodInvocation,29",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "T data,SingleVariableDeclaration,49",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "String msg,SingleVariableDeclaration,49",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "newResult(data,CommonConstants.SUCCESS,msg),MethodInvocation,50",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "userMapper.insert(user),MethodInvocation,30",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					],
					links: [
					  {
						source: "bCryptPasswordEncoder.encode(user.getPassword()),MethodInvocation,25",
						target: "user.getPassword(),MethodInvocation,25",
						value:0.7,
						type:'嵌套调用',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						target: "bCryptPasswordEncoder.encode(user.getPassword()),MethodInvocation,25",
						value:0.7,
						type:'嵌套调用',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setCreated(new Date()),MethodInvocation,27",
						target: "new Date(),ClassInstanceCreation,27",
						value:0.7,
						type:'嵌套调用',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "R.success(),MethodInvocation,29",
						target: "T data,SingleVariableDeclaration,49",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "newResult(data,CommonConstants.SUCCESS,msg),MethodInvocation,50",
						target: "R.success(),MethodInvocation,29",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						}
					  },
					  {
						source: "@RequestBody User user,SingleVariableDeclaration,24",
						target: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						target: "user.setRole(\"ROLE_USER\"),MethodInvocation,26",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setRole(\"ROLE_USER\"),MethodInvocation,26",
						target: "user.setCreated(new Date()),MethodInvocation,27",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setCreated(new Date()),MethodInvocation,27",
						target: "userService.save(user),MethodInvocation,28",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "userService.save(user),MethodInvocation,28",
						target: "R.success(),MethodInvocation,29",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "T data,SingleVariableDeclaration,49",
						target: "String msg,SingleVariableDeclaration,49",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "String msg,SingleVariableDeclaration,49",
						target: "newResult(data,CommonConstants.SUCCESS,msg),MethodInvocation,50",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "userService.save(user),MethodInvocation,28",
						target: "userMapper.insert(user),MethodInvocation,30",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "userMapper.insert(user),MethodInvocation,30",
						target: "userService.save(user),MethodInvocation,28",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						}
					  }
					],
					roam: true,   //添加缩放和移动
					draggable: true,
					emphasis: {
					  itemStyle: {
						shadowBlur: 10,
						shadowOffsetX: 0,
						shadowColor: "rgba(0, 0, 0, 0.5)",
					  }
					},
				  },
				],
			},
			option1: {
				title: {
				  text: "对象生成及方法调用",
				  left: "center",
				},
				tooltip: {
				  trigger: "item"
				},
				series: [
				  {
					name: "对象及方法调用",
					type: "graph",
					layout:'force',
					edgeSymbol:['','arrow'],
					label:{
					  show:true
					},
					force:{
					  repulsion:1000,
					  edgeLength: [100,200]
					},
					draggable:true,
					data: [
					  {
						name: "@RequestBody User user,SingleVariableDeclaration,24",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "user.getPassword(),MethodInvocation,25",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "bCryptPasswordEncoder.encode(user.getPassword()),MethodInvocation,25",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "user.setRole(\"ROLE_USER\"),MethodInvocation,26",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "new Date(),ClassInstanceCreation,27",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "user.setCreated(new Date()),MethodInvocation,27",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "userService.save(user),MethodInvocation,28",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "R.success(),MethodInvocation,29",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					  {
						name: "T data,SingleVariableDeclaration,49",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "String msg,SingleVariableDeclaration,49",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "newResult(data,CommonConstants.SUCCESS,msg),MethodInvocation,50",
						fixed : false,
						itemStyle: {
							color: '#fc853e'
						},
						symbolSize: 20
					  },
					  {
						name: "userMapper.insert(user),MethodInvocation,30",
						fixed : false,
						itemStyle: {
							color: '#A9A9A9'
						},
						symbolSize: 20
					  },
					],
					links: [
					  {
						source: "bCryptPasswordEncoder.encode(user.getPassword()),MethodInvocation,25",
						target: "user.getPassword(),MethodInvocation,25",
						value:0.7,
						type:'嵌套调用',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						target: "bCryptPasswordEncoder.encode(user.getPassword()),MethodInvocation,25",
						value:0.7,
						type:'嵌套调用',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setCreated(new Date()),MethodInvocation,27",
						target: "new Date(),ClassInstanceCreation,27",
						value:0.7,
						type:'嵌套调用',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "R.success(),MethodInvocation,29",
						target: "T data,SingleVariableDeclaration,49",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "newResult(data,CommonConstants.SUCCESS,msg),MethodInvocation,50",
						target: "R.success(),MethodInvocation,29",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						}
					  },
					  {
						source: "@RequestBody User user,SingleVariableDeclaration,24",
						target: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setPassword(bCryptPasswordEncoder.encode(user.getPassword())),MethodInvocation,25",
						target: "user.setRole(\"ROLE_USER\"),MethodInvocation,26",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setRole(\"ROLE_USER\"),MethodInvocation,26",
						target: "user.setCreated(new Date()),MethodInvocation,27",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "user.setCreated(new Date()),MethodInvocation,27",
						target: "userService.save(user),MethodInvocation,28",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "userService.save(user),MethodInvocation,28",
						target: "R.success(),MethodInvocation,29",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "T data,SingleVariableDeclaration,49",
						target: "String msg,SingleVariableDeclaration,49",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "String msg,SingleVariableDeclaration,49",
						target: "newResult(data,CommonConstants.SUCCESS,msg),MethodInvocation,50",
						value:0.7,
						type:'顺序执行',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "userService.save(user),MethodInvocation,28",
						target: "userMapper.insert(user),MethodInvocation,30",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						},
					  },
					  {
						source: "userMapper.insert(user),MethodInvocation,30",
						target: "userService.save(user),MethodInvocation,28",
						value:0.3,
						type:'外部文件',
						label: {
							normal: {
							   show: true,
							   formatter: function(x){return x.data.type;}
								   }
						}
					  }
					],
					roam: true,   //添加缩放和移动
					draggable: true,
					emphasis: {
					  itemStyle: {
						shadowBlur: 10,
						shadowOffsetX: 0,
						shadowColor: "rgba(0, 0, 0, 0.5)",
					  }
					},
				  },
				],
			},
			inlinks : [],
			outlinks : [],
			repoPath:'1autodidact\communitycode',
			fileName:[
			{
				fileName:' UserService.java',
				filePath:'',
				method:' userService.save()',
			},
			{
				fileName:' AuthorizeController.java',
				filePath:'',
				method:` AuthorizeController.
						registerUser()`
			}
			],
			
			imgsrc: require('../page/b.png'),
			codepiece:'',
			codefile:'',
			fileNameshow:'AuthController.java',
			javademo:[
					`@PostMapping("/register")
					public R registerUser(@RequestBody User user){
						user.setPassword(bCryptPasswordEncoder.encode(user.getPassword()));
						user.setRole("ROLE_USER");
						user.setCreated(new Date());
						userService.save(user);
						return R.success();
					}`,
						`public static <T> R<T> success() {
						return newResult(null, CommonConstants.SUCCESS, CommonConstants.SUCCESS_MESSAGE);
					}`],
			javaFull:[
					`package com.github.health.check.controller;

					import com.github.health.check.domain.entity.User;
					import com.github.health.check.service.UserService;
					import com.github.health.check.util.R;
					import org.springframework.beans.factory.annotation.Autowired;
					import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
					import org.springframework.web.bind.annotation.PostMapping;
					import org.springframework.web.bind.annotation.RequestBody;
					import org.springframework.web.bind.annotation.RestController;

					import java.util.Date;

					@RestController
					public class AuthController {

						@Autowired
						private UserService userService;

						@Autowired
						private BCryptPasswordEncoder bCryptPasswordEncoder;

						@PostMapping("/register")
						public R registerUser(@RequestBody User user){
							user.setPassword(bCryptPasswordEncoder.encode(user.getPassword()));
							user.setRole("ROLE_USER");
							user.setCreated(new Date());
							userService.save(user);
							return R.success();
						}
					}
					`,
					`package com.github.health.check.util;

					import com.github.health.check.constant.CommonConstants;
					import java.io.Serializable;


					public class R<T> implements Serializable {

						private static final long serialVersionUID = 1L;

						private int code;

						private String msg;

						private T data;

						public int getCode() {
							return code;
						}

						public void setCode(int code) {
							this.code = code;
						}

						public String getMsg() {
							return msg;
						}

						public void setMsg(String msg) {
							this.msg = msg;
						}

						public T getData() {
							return data;
						}

						public void setData(T data) {
							this.data = data;
						}

						public static <T> R<T> success() {
							return newResult(null, CommonConstants.SUCCESS, CommonConstants.SUCCESS_MESSAGE);
						}

						public static <T> R<T> success(T data) {
							return newResult(data, CommonConstants.SUCCESS, CommonConstants.SUCCESS_MESSAGE);
						}

						public static <T> R<T> success(T data, String msg) {
							return newResult(data, CommonConstants.SUCCESS, msg);
						}

						public static <T> R<T> failed() {
							return newResult(null, CommonConstants.FAIL, CommonConstants.FAIL_MESSAGE);
						}

						public static <T> R<T> failed(String msg) {
							return newResult(null, CommonConstants.FAIL, msg);
						}

						public static <T> R<T> failed(T data) {
							return newResult(data, CommonConstants.FAIL, CommonConstants.FAIL_MESSAGE);
						}

						public static <T> R<T> failed(T data, String msg) {
							return newResult(data, CommonConstants.FAIL, msg);
						}

						public static <T> R<T> failed(T data, int code, String msg) {
							return newResult(data,code, msg);
						}

						private static <T> R<T> newResult(T data, int code, String msg) {
							R<T> result = new R<>();
							result.setCode(code);
							result.setData(data);
							result.setMsg(msg);
							return result;
						}

					}
`
			]
			}
		},
	changeConcept(params){
      if( params.dataType=='node'){
      console.log(params.name);
      }
      
    },
	
	created() {
		this.codepiece=this.javademo[1];
		this.codefile=this.javaFull[1];
		this.fileNameshow='R.java';
		this.option=this.option1;	
		
	},
	mounted(){  //页面初始化方法
	  Prism.highlightAll()
	  const that = this
		window.addEventListener('resize', function() {
		  that.echarts.resize() //初始化的
		} )
	 },
	watch:{
     codefile:{//深度监听，可监听到对象、数组的变化
         handler(val, oldVal){
         },
         deep:true //true 深度监听
     },
     codepiece:{//深度监听，可监听到对象、数组的变化
         handler(val, oldVal){
         },
         deep:true //true 深度监听
     }
	},
	methods: {
	exchangecode(title){
		this.$router.push('/codepage');		
	}
	}
}
</script>

<style>
.mainpageblock{
}
.link{
	position:relative;
	margin-top:50px;
	margin-left:20px;
	font-size:20px;
}
.title{
	position:relative;
	margin-top:20px;
	margin-left:20px;
	font-size:25px;
}
.fileitem{
	position:relative;
	margin-top:10px;
	margin-left:20px;
	font-size:20px;
}
.owncode{  
  overflow: auto;
  overflow-x: scroll;
  white-space: nowrap;
  right:5px;
  width:100%;  
  height:auto;
  top:50px;
  left:2%;
  position: relative; 
  z-index:1;
}
.casecard{
	background-color:#909399;
	border-radius: 30px;
	font-family:"黑体";
	font-weight: 3px;
	font-size:x-large;
    position: relative;
    color:#909399;
	top:30px;
	left:25px;
}
.container {
  width: 100%;
  height: 400px;
}
.chart {
  left: 0%;
  top: 0%;
  width: 100%;
  height:100%;
}
.el-row {
  margin-bottom: 20px;
  top:20px;
  bottom: 0%;
  marginRight:20px;
  width:100%;
  left:20px;
  position: relative; 
  z-index:1;
}
.el-row ::-webkit-scrollbar {
    width: 0;
}
.el-row  > ul {
    height: 100%;
}
.my-editor {
 background: #2d2d2d;
 color: #ccc;
 
 font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
 font-size: 14px;
 line-height: 1.5;
 padding: 5px;
}
 
/* optional */
.prism-editor__textarea:focus {
 outline: none;
}
 
/* not required: */
.height-300 {
 height: 300px;
}
</style>
