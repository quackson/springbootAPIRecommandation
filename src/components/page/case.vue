
<template>
<div>
<el-row :gutter="20">
<el-breadcrumb separator-class="el-icon-arrow-right" style="font-size:20px;left:20px;position:absolute">
	  <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
	  <el-breadcrumb-item>PostMapping()</el-breadcrumb-item>
	  <el-breadcrumb-item>选择使用场景</el-breadcrumb-item>
	</el-breadcrumb>
<el-col :span="24">	
	<el-row>
	<div class="casecard">
	  <el-col :span="7" v-for="item in case2" :index="item.index" :key="item.index">
		<el-card :body-style="{ padding: '0px' }" shadow="hover" style="background-color:#C0C4CC;marginLeft:10px;">
		  <div style="padding: 14px;">
			<i :class="item.icon"></i>
			<span>{{item.title}}</span>
			<div class="bottom clearfix">
			</div>
		  </div>
		  <div style="font-size:15px;padding:10px;">
			<span>{{item.content}}</span>
			<div class="bottom clearfix">
			</div>
		  </div>
		</el-card>
	 </el-col>
	</div>
	</el-row>
	<el-row>
	<div class="casecard">
	  <el-col :span="5" v-for="item in cases" :index="item.index" :key="item.index">
		<el-card :body-style="{ padding: '0px'}" shadow="hover" style="background-color:#C0C4CC;marginLeft:30px;">
		  <div style="padding: 14px;">
			<i :class="item.icon"></i>
			<span>{{item.title}}</span>
		  </div>
		  <div style="font-size:15px;padding:10px;">
			<span>{{item.content}}</span>
			<div class="bottom clearfix">
			</div>
		  </div>
		</el-card>
	 </el-col>
	</div>
	</el-row>
	<div class="repolist">
		<el-table
		:data="tableData"
		stripe
		style="width: 100%;line-height:20px;"
		:row-class-name="tableRowClassName"
		:row-style="{height:'30px'}"
		:cell-style="{padding: '0'}">
		<el-table-column
		  prop="name"
		  label="name"
		  width="360">
		  <template slot-scope="scope">
            <el-button type="text" 
			@click="openDialog(scope.row)"
			>
			{{ scope.row.name}}
			</el-button>
          </template>
		</el-table-column>
		<el-table-column
		  prop="author"
		  label="author"
		  width="360">
		</el-table-column>
		<el-table-column
		  prop="userapi"
		  label="URL">
		</el-table-column>
		<el-table-column
		  prop="file"
		  label="controllerFile">
		</el-table-column>
	  </el-table>
	</div>
</el-col>
</el-row>	
</div>
</template>


<script>
export default {
 data() {		
	    return {
		cases:[
		{
			title:' register',
			icon:'el-icon-user',
			content:`keyword:email,username,password,id,
			...`
		},
		{
			title:' login',
			icon:'el-icon-s-fold',
			content:`keyword:
			email,username,password,id
			auth...`
		},
		{
			title:' logout',
			icon:'el-icon-s-unfold',
			content:`keyword:
			email,username,password,id
			auth...`
		},
		{
			title:' search',
			icon:'el-icon-search',
			content:`keyword:key,type,find,lable,input,
			record...`
		}
		],
        tableData:[
		{
			name:'13101144/health-check',
			author:'13101144',
			userapi:'registeruser',
			file:'AuthController.java'
		},
		{
			name:'1autodidact/communitycode',
			author:'1autodidact',
			userapi:'register',
			file:'AuthorizeController.java'
		},
		{
			name:'201206030/novel-cloud',
			author:'201206030',
			userapi:'register',
			file:'RegisterController.java'
		},
		{
			name:'Ahaochan/project',
			author:'Ahaochan',
			userapi:'register',
			file:'UserController.java'
		},
		{
			name:'Ahuijava1/word_project',
			author:'Ahuijava1',
			userapi:'register',
			file:'RegisterController.java'
		},
		{
			name:'GodLikeZeal/zealsay_backend',
			author:'GodLikeZeal',
			userapi:'register',
			file:'AuthController.java'
		},
		{
			name:'jeesun/oauthserver',
			author:'jeesun',
			userapi:'register',
			file:'UserController.java'
		},
		{
			name:'lzpeng723/minimal-boot',
			author:'lzpeng723',
			userapi:'register',
			file:'UserRestService.java'
		},
		{
			name:'mangalaxy/mango',
			author:'mangalaxy',
			userapi:'register',
			file:'RegisteredClientAuthenticationService.java'
		}
		],	
		case2:[
		{
			title:' upload',
			icon:'el-icon-upload2',
			content:`keyword:
			picture,txt,log,
			information...`
		},
		{
			title:' add',
			icon:'el-icon-circle-plus-outline',
			content:`keyword:
			user,id,new,
			student...`
		},
		{
			title:' delete',
			icon:'el-icon-remove-outline',
			content:`keyword:
			user,id,new,
			item...`
		}],
		tableHeight: window.innerHeight  - 100,
        currentPage:1,
        pageSize:10,
		totalNum:100, 
		 k:'0',
		 m:'0',
		 way:'origin',
		 loadcomplete:false,
      }
    },	
   methods: {
        ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
	handleSizeChange(val) {
                   console.log(`每页 ${val} 条`);
                   this.pageSize = val;    //动态改变
	},
	changetable(page){
		var begin=(page-1)*this.pageSize;
				  //加载val页信息
		let _this=this
		this.$http.request({
				  url:_this.$url + '/searchPaper?method='+_this.way+'&query='+_this.k +'&maxNum='+_this.pageSize+'&start='+begin,
				  method:'get',
				}).then(function(response) {
				  _this.tableData = response.data.papers,
				 _this.loadcomplete=true,
				  //console.log(begin),
				  //console.log(response.data.papers),
				  console.log(_this.tableData)
				}).catch(function(error) {
				  console.log(error)
				});
				
				//获取论文列表个数
				this.$http.request({
				  url:_this.$url + '/getPaperNum?method='+ _this.way+'&query='+_this.k ,
				  method:'get',
				}).then(function(response) {
				//console.log(response),
				   _this.totalNum=response.data.num,
				   console.log('获取论文列表个数'),
				   console.log(_this.totalNum)
				}).catch(function(error) {
				  console.log(error)
				});
	},
     handleCurrentChange(val) {
                   console.log(`当前页: ${val}`);				   	  
				 this.currentPage = val;
				//console.log(this.tabelData);
    },
	openDialog (paper) {
		console.log(`dash: ${paper.pdfLink}`);
		  /*
		  this.$router.push({
          name: 'readpage',
          params: {url:paper.pdfLink,id:paper.id}
		  });
		  */
		  this.$router.push('/codepage');
		 },
		 getData(qstr){
				this.k=qstr.k;
				this.m=qstr.m;
				if(this.m=='1')
				{
					this.way="ti";
				}
				if(this.m=='2')
				{
					this.way='au';
				}
				if(this.m=='3')
				{
					this.way='abs';
				}
				if(this.m=='4')
				{
					this.way='cat';
				}
				let _this = this	
				//加载列表首页信息
				this.changetable(1);
		 },
   },
   watch: {
    '$route' (to, from) {
		this.tabelData=new Array(this.pageSize);
        this.getData(this.$route.query);
		},
	currentPage(newv, oldv) {
		console.log("in watch");
		console.log(newv);
        this.changetable(newv);
		},
		
	},
	created(){
		//this.tabelData=new Array(this.pageSize);
		//this.getData(this.$route.query);
		//this.page=(this.tabelData.length)/13+((this.tabelData.length%13==0)?0:1)
		this.totalNum=this.tabelData.length;
		this.pageSize=13;
	},   
}
</script>
<style>
.repolist{
	background-color:#(0,0,0,1);
	font-family:"黑体";
    position: relative;
	margin-top:80px;
	bottom:0px;
	width:90%;
	left:5%;
	line-height:10px;
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
.el-tooltip__popper{max-width:40%}
</style>
<style scoped>
 .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

.el-row {
  margin-bottom: 20px;
  top:20px;
  bottom: 4%;
  right:0px;
  width:100%;
  left:10px;
  position: relative; 
  z-index:1;
}
.el-row ::-webkit-scrollbar {
    width: 0;
}
.el-row  > ul {
    height: 100%;
}
.block{
	/*
  bottom:0px;
  left: 800px;
  position:fixed;
  z-index:1;
  */
  bottom:0px;
  left: 50%;
  position:fixed;
  z-index:1;
}
</style>