
<template>
<div class="mainpageblock">
<el-row :gutter="22">
		<el-breadcrumb separator-class="el-icon-arrow-right" style="font-size:20px;left:20px;position:absolute">
		  <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
		  <el-breadcrumb-item :to="{ path: '/dashboard' }">{{api}}</el-breadcrumb-item>
		  <el-breadcrumb-item>{{projectName}}</el-breadcrumb-item>
		</el-breadcrumb>
	<el-col :span="13">
		<div class="owncode" v-infinite-scroll="load">
				 
			<pre  class="language-java line-numbers" style="white-space:pre-wrap;">
<code class="language-java">{{codepiece}}</code>
			</pre>
				
		</div>
		<div class="owncode" v-infinite-scroll="load" >
				<div style="font-size:15px;white-space:pre-wrap;"></div>
				<pre  class="language-java line-numbers">
<code>{{codefile}}</code>
				</pre>
		</div>
	</el-col>
	<el-col :span="9">
		<div class="fileFolder">			
			<el-tree :data="dirs" :props="defaultProps" @node-click="exchangecode" style="background-color:#F0F8FF;font-size:30px;"></el-tree>
		</div>
		<div class="api">			
			<el-tree :data="apis" :props="defaultProps" @node-click="changeAPI" style="background-color:#F0F8FF;font-size:30px;"></el-tree>
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
			api:'',
			apis:[
				{
					'label':'PostMapping',
					'package':'org.springframework.web.bind.annotation',
					'url':'https://docs.spring.io/spring-framework/docs/current/javadoc-api/',
				},
				{
					'label':'RequestBody',
					'package':'',
					'url':'https://docs.spring.io/spring-framework/docs/current/javadoc-api/',
				}
			],
			activeNames: ['1'],
			dirs:[],
			methodName:'',			
			codepiece:'',
			codefile:'',
			fileName:'',
			projectName:'',
			fullapi:[],
			id:''
			}
		},
	changeConcept(params){
      if( params.dataType=='node'){
      console.log(params.name);
      }
      
    },
	
	created() {
		this.fileNameshow=this.$route.params.projectName;
		this.api=this.$route.params.method;
		this.projectName=this.$route.params.projectName;
		this.id=this.$route.params.caseID;
		var _this=this
		var ID=this.$route.params.caseID;
		console.log('created code page')

		var piece_ori=''
		var file_ori=''
		this.$http.request({
				  url:_this.$url + '/opencase?caseID='+ID,
				  method:'get',
				}).then(function(response) {
				  console.log(response),
				  _this.codepiece = response.data.codepiece,
				  _this.dirs=response.data.dirs,
				  _this.codefile= response.data.codefile,
				  _this.apis= response.data.apis,
				  _this.fullapi= response.data.fullapi,
				  console.log(_this.apis)
				}).catch(function(error) {
				  console.log(error)
			});	
		
		
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
		exchangecode(item){
			console.log(item);
			var this_=this;
			var fileID=item.fileID;
			this.$http.request({
				  url:this_.$url + '/openfilebyid?fileID='+fileID+'&caseID='+this_.id,
				  method:'get',
				}).then(function(response) {
				  console.log(response),
				  this_.codepiece = response.data.codefile,
				  this_.codefile= response.data.codefile,
				  this_.apis= response.data.apis,
				  console.log(this_.apis)
				}).catch(function(error) {
				  console.log(error)
			});	
		},
		handleChange(val) {
			console.log(val);
		}
	}
}
</script>

<style>
.link{
	position:relative;
	margin-top:50px;
	margin-left:20px;
	font-size:20px;
}
.title{
	position:relative;
	margin-top:5%;
	margin-left:5%;
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
.container {
  width: 100%;
  height: 500px;
}
.chart {
  margin-left: 10%;
  margin-top: 5%;
  width: 100%;
  height:100%;
}
.el-row {
  margin-bottom: 20px;
  top:20px;
  bottom: 0%;
  margin-right:20px;
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
.fileFolder{
  right:5px;
  width:100%;  
  height:auto;
  margin-top:10%;
  background: #F0F8FF;
  font-size:30px;
  font-family:Georgia;
  left:10%;
  position: relative; 
  z-index:1;
}
.api{
  right:5px;
  width:100%;  
  height:auto;
  margin-top:10%;
  background-color: #F0F8FF;
  font-size:30px;
  font-family:Georgia;
  left:10%;
  position: relative; 
  z-index:1;
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
