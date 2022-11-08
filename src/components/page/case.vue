
<template>
<div>
<el-row :gutter="20">
<el-breadcrumb separator-class="el-icon-arrow-right" style="font-size:20px;left:20px;position:absolute">
	  <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
	  <el-breadcrumb-item :to="{ path: '/dashboard' }">{{api.api}} </el-breadcrumb-item>
	  <el-breadcrumb-item>选择使用场景</el-breadcrumb-item>
</el-breadcrumb>
	<el-row>            
		                
		<div style="margin-top:3%;width:100%;margin-left:2%">     
		<el-col :span="2" v-for="(item) in cases" :key="item.title" :offset="1" >               
			<el-card :body-style="{ padding: '1px'}" shadow="hover" style="background-color:#F0F8FF;">                    
				<div class="cardpiece" >                    
					<div class="title" style="text-align:center;font-size:20px;font-family:Lucida Handwriting">
						{{item.title}}
					</div>
					<div class="discription" style="margin-left:2%;margin-right:2%;margin-top:5%;font-size:17px;word-break:break-all;font-family:Georgia">
						{{item.content}}
					</div>	
					<div class="detail" style="margin-left:2%;margin-right:2%;margin-top:5%;font-size:17px;word-break:break-all;font-family:Georgia">
						detail:{{item.child}}
					</div>				
				</div>                
			</el-card>            
		</el-col>               
		</div>         
		</el-row> 
	<el-row>
	<div class="choose">
	  <el-cascader :options="options" @change="getchoose" style="width:30%;font-size:15px;height:8%"></el-cascader>
	</div>
	</el-row>
	<div class="repolist">
		<el-table 
		:data="showData"
		stripe
		style="width: 100%;font-size: 20px;font-family:Georgia"
		:row-class-name="tableRowClassName"
		:row-style="{height:'50px'}"
		:cell-style="{padding: '0'}">
		<template slot="empty">
                    请选择使用场景
		</template>
		<el-table-column
		  prop="projectName"
		  label="GitHub repository name"
		  width="360">
		  <template slot-scope="scope">
            <el-button type="text" 
			@click="openDialog(scope.row)"
			>
			{{ scope.row.projectName}}
			</el-button>
          </template>
		</el-table-column>
		<el-table-column
		  prop="methodName"
		  label="URL">
		</el-table-column>
		<el-table-column
		  prop="className"
		  label="controllerFile">
		</el-table-column>
	  </el-table>
	</div>
</el-row>	
</div>
</template>


<script>
export default {
 data() {		
	    return {
	    options: [
	    {
          value: '0',
          label: 'register',
          disabled: true,
          children: [
          	{
            	value: '0',
            	label: 'email',
          		disabled: true,
          		cases:[]
          	},{
           		value: '1',
            	label: 'phone',
          		disabled: true,
          		cases:[]
          	}], 
        },{
          value: '1',
          label: 'add',
          disabled: true,
          children: [
          	{
            	value: '0',
            	label: 'user',
          		disabled: true,
          		cases:[]
          	},{
            	value: '0',
            	label: 'permission',
          		disabled: true,
          		cases:[]
          	},{
            	value: '0',
            	label: 'comment',
          		disabled: true,
          		cases:[]
          	},{
            	value: '0',
            	label: 'admin',
          		disabled: true,
          		cases:[]
          	},] 
        }, {
          value: '0',
          label: 'delete',
          disabled: true,
          children: [
          	{
            	value: '0',
            	label: 'user',
          		disabled: true,
          		cases:[]
          	}, {
           		value: '1',
            	label: 'article',
          		disabled: true,
          		cases:[]
          	},{
            	value: '1',
            	label: 'permission',
          		disabled: true,
          		cases:[]
          	},
          	] 
        },{
          value: 'zhinan',
          label: 'upload',
          disabled: true,
          children: [
          	{
            	value: 'shejiyuanze',
            	label: 'file',
          		disabled: true,
          		cases:[]
          	}, {
            	value: 'daohang',
            	label: 'image',
          		disabled: true,
          		cases:[]
          	},{
            	value: 'daohang',
           		label: 'avatar',
          		disabled: true,
          		cases:[]
          	}] 
        },{
          value: 'zhinan',
          label: 'login',
          disabled: true,
          children: [
          	{
            	value: 'shejiyuanze',
            	label: 'success',
          		disabled: true,
          		cases:[]
          	}, {
            	value: 'daohang',
            	label: 'error',
          		disabled: true,
          		cases:[]
          	}] 
        },{
          value: 'zhinan',
          label: 'logout',
          disabled: true,
          children: [
          	{
            	value: 'shejiyuanze',
            	label: 'success',
          		disabled: true,
          		cases:[]
          	}, {
            	value: 'daohang',
            	label: 'error',
          		disabled: true,
          		cases:[]
          	}] 
        },{
          value: 'zhinan',
          label: 'search',
          disabled: true,
          children: [
          	{
            	value: 'shejiyuanze',
            	label: 'by',
          		disabled: true,
          		cases:[]
          	}, {
            	value: 'daohang',
            	label: 'page',
          		disabled: true,
          		cases:[]
          	},{
            	value: 'daohang',
            	label: 'user',
          		disabled: true,
          		cases:[]
          	}] 
        }],
		cases:[
		{
			title:' register',
			icon:'el-icon-user',
			exist:false,
			content:`new user visit when account needed
			...`,
			child:'with email, with phone'
		},
		{
			title:' login',
			icon:'el-icon-s-fold',
			exist:true,
			content:`user get in with account already
			...`,
			child:'success,error'
		},
		{
			title:' logout',
			icon:'el-icon-s-unfold',
			exist:true,
			content:`user get out with account exit
			...`,
			child:'succes,error'
		},
		{
			title:' search',
			icon:'el-icon-search',
			exist:true,
			content:`search data with keyword or page
			...`,
			child:'with key, with page, user'
		},
		{
			title:' upload',
			icon:'el-icon-upload2',
			exist:true,
			content:`upload file ,image or something provided by users
			...`,
			child:'image, avatar, file'
		},
		{
			title:' add',
			icon:'el-icon-circle-plus-outline',
			exist:true,
			content:`add new data to database
			...`,
			child:'user, permission, admin, comment'
		},
		{
			title:' delete',
			icon:'el-icon-remove-outline',
			exist:true,
			content:`delete existed item
			...`,
			child:'user, article, permission'
		}
		],
        tableData:[],	
		api:{
			api:'不指定API',
			package:''
		},
		showData:[],
		tableHeight: window.innerHeight  - 100,
        currentPage:1,
        pageSize:10,
		showif:false,
		totalNum:100, 
		 k:'0',
		 m:'0',
		 way:'origin',
		 loadcomplete:false,
      }
    },	
   methods: {
   	getchoose (node) {      
	  //node[0] 下标，node[1]下标
	   console.log(this.$url)
	  	console.log(this.options[node[0]].children[node[1]])
		var temp=[];
		var key=this.options[node[0]].label;
		var subkey=this.options[node[0]].children[node[1]].label;
		if(! typeof(this.options[node[0]].children[node[1]].cases)=='undefined'){
			let _this=this
			console.log(_this.options[node[0]].children[node[1]].cases);
			var str_=_this.options[node[0]].children[node[1]].cases[0];
			if(_this.options[node[0]].children[node[1]].cases.length>1){
				for(var i=1;i<_this.options[node[0]].children[node[1]].cases.length;i++){
					str_=str_+'~'+_this.options[node[0]].children[node[1]].cases[i];
				}
			}
			console.log(str_)
			this.$http.request({
				  url:_this.$url + '/getcasebylist?cases='+str_+'&key='+key+'&sub='+subkey,
				  method:'get',
				}).then(function(response) {
				  console.log(response),
				  _this.showData = response.data.cases
				}).catch(function(error) {
				  console.log(error)
			});
			
		}
		else{
			let _this=this
			this.$http.request({
				  url:_this.$url + '/getcasebylist?key='+key+'&sub='+subkey,
				  method:'get',
				}).then(function(response) {
				  console.log(response),
				  _this.showData = response.data.cases
				}).catch(function(error) {
				  console.log(error)
			});
		}
		
	    
	},
        ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
	handleSizeChange(val) {
                   console.log(`每页 ${val} 条`);
                   this.pageSize = val;    //动态改变
	},
	changetable(page){
		
	},
     handleCurrentChange(val) {
    },
	openDialog (item) {
		console.log(item);
		var this_=this;
		console.log(this_.api)
		this.$router.push({name:'codepage',
		  				   params:{
							caseID:item.caseID,
							projectName:item.projectName,
							method:this_.api.api
							}
		  				})
	},

	showitem(title){
		console.log(title);
		var temp=[];
		if (title==" register")
		{
			console.log(" resgiter!")
			for(var i=0;i<this.tableData[0].length;i++){
				temp.push(this.tableData[0][i])
			}
		}
		else if (title==" add")
		{
			console.log(" add!")
			for(var i=0;i<this.tableData[1].length;i++){
				temp.push(this.tableData[1][i])
			}
		}
		this.showData=temp;
	}
   },
   watch: {
    '$route' (to, from) {
		this.tableData=new Array(this.pageSize);
        this.getData(this.$route.query);
		},
	currentPage(newv, oldv) {
		console.log("in watch");
		console.log(newv);
        this.changetable(newv);
		},
		
	},
	created(){
		if(this.$route.params.api){
			//console.log(this.$route.params);
			this.api.api=this.$route.params.api+"()";
			var cases=this.$route.params.case.cases;
			///console.log(this.api.api);
			//console.log(cases.length);
			for(var i=0;i<cases.length;i++){
				var OneCase=cases[i];
				var key=OneCase.key;
				var subkey=OneCase.sub;
				var caseID=OneCase.caseID;
				//console.log(key)
				//console.log(subkey)
				//console.log(caseID)
				for(var j=0;j<this.options.length;j++){
					if (this.options[j].label==key){
						this.options[j].disabled=false;
						for(var k=0;k<this.options[j].children.length;k++){
							//console.log(this.options[j].children[k]);
							if (this.options[j].children[k].label==subkey){
								this.options[j].children[k].disabled=false;
								if (this.options[j].children[k].cases.indexOf(caseID)==-1){
									this.options[j].children[k].cases.push(caseID)
								}								
							}
						}
					}
				}

			}
		}
		else{
			for(var j=0;j<this.options.length;j++){
					this.options[j].disabled=false;
					for(var k=0;k<this.options[j].children.length;k++){
					this.options[j].children[k].disabled=false;
					}
				}
			
		}
		this.totalNum=this.tableData.length;
		this.pageSize=10;
	},   
}
</script>
<style>
.repolist{
	ground-color:#(0,0,0,back1);
	font-family:"黑体";
    position: relative;
	margin-top:80px;
	margin-bottom:0px;
	width:90%;
	margin-left:5%;
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
	margin-top:10px;
	margin-left:40px;
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
  margin-bottom: 1%;
  margin-right:0px;
  width:100%;
  margin-left:10px;
  position: relative; 
  z-index:1;
}
.block{
  margin-bottom:0px;
  margin-left: 50%;
  position:relative;
  z-index:1;
}
.choose{
  margin-top:5%;
  margin-left: 40%;
  width:60%;
  position:relative;
  z-index:1;
}
</style>