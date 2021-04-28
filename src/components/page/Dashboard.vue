
<template>
<div>
<el-row :gutter="20">
<el-col :span="24">
	<el-breadcrumb separator-class="el-icon-arrow-right" style="font-size:20px;left:20px;position:absolute">
	  <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
	  <el-breadcrumb-item>选择单API</el-breadcrumb-item>
	</el-breadcrumb>
	<el-row class="demo-autocomplete">
	<div class="searchblock">
		<el-autocomplete
		  class="inline-input"
		  style="width:30%;background-color:#DCDFE6"
		  v-model="state2"
		  prefix-icon="el-icon-search"
		  :fetch-suggestions="querySearch"
		  placeholder="PostMapping"
		  :trigger-on-focus="false"
		  @select="handleSelect"
		></el-autocomplete>
	</div>
	<div class="apilist">
		<el-table
		:data="tableData"
		stripe
		style="width: 100%;line-height:20px;background-color:#909399;height:580px;"
		:row-class-name="tableRowClassName"
		:row-style="{height:'30px'}"
		:cell-style="{padding: '0'}">
		<el-table-column
		  prop="api"
		  label="api"
		  width="360">
		  <template slot-scope="scope">
            <el-button type="text" 
			@click="openDialog()"
			>
			{{ scope.row.api}}
			</el-button>
          </template>
		</el-table-column>
		<el-table-column
		  prop="class"
		  label="class"
		  width="360">
		</el-table-column>
		<el-table-column
		  prop="package"
		  label="package">
		</el-table-column>
	  </el-table>
	</div>
</el-row>
	
</el-col>	
</el-row>
	<div class="block">
		<el-pagination
		@size-change="handleSizeChange"
		@current-change="handleCurrentChange"
		:current-page.sync="currentPage"
		:page-size="pageSize"
		background
		layout="prev, pager, next, jumper"
		:total="totalNum">
		</el-pagination>
	</div>
</div>
</template>


<script>
export default {
 data() {		
	    return {
		restaurants: [],
        state1: '',
        state2: '',
        tableData: [
			{
				'api':'PostMapping()',
				'class':'RequestMapping',
				'package':'org.springframework.web.bind.annotation.RequestMapping'
			}
		],
		tableHeight: window.innerHeight  - 100,
        currentPage:1,
        pageSize:1,
		totalNum:1, 
		username:'',
		loadcomplete:false,
      }
    },	
   methods: {
    tableRowClassName({row, rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 3) {
          return 'success-row';
        }
        return '';
      },
        ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
	handleSizeChange(val) {
                   console.log(`每页 ${val} 条`);
                   this.pageSize = val;    //动态改变
	},
     handleCurrentChange(val) {
                //console.log(`当前页: ${val}`);	
				console.log(this.totalNum);
				console.log((val-1)*this.pageSize);
				if(this.totalNum<=(val-1)*this.pageSize)
				{
					_this.$message({
                    message: "超出最大页码",
                    type: 'warning',
					});
					return;
				}
				 this.currentPage = val;
    },
	openDialog () {
		  this.$router.push('/codepage');
		 },
		 getData(qstr){
				this.username=localStorage.getItem('ms_username')
				let _this=this
				this.$http.request({
				  url:_this.$url + '/getRecommendation?user='+_this.username,
				  method:'get',
				}).then(function(response) {
				//console.log(response.data),
				  _this.tableData = response.data.papers,
				  _this.totalNum= response.data.len,
				  _this.loadcomplete=true,
				  console.log(_this.tableData)
				  //console.log(_this.totalNum)
				}).catch(function(error) {
				  console.log(error)
				});		
		 },
		 defaultdata(){	
					let _this=this
					this.$http.request({
					  url:_this.$url + '/searchPaper?method=cat&query=cs.AI&maxNum=10',
					  method:'get',
					}).then(function(response) {
					//console.log(response.data),
					  _this.tableData = response.data.papers,
					  _this.totalNum= response.data.num,
					  _this.loadcomplete=true,
					  console.log(_this.tableData)
					  //console.log(_this.totalNum)
					}).catch(function(error) {
					  console.log(error)
					});
		 },
		  querySearch(queryString, cb) {
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
        // 调用 callback 返回建议列表的数据
        cb(results);
      },
      createFilter(queryString) {
        return (restaurant) => {
          return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadAll() {
        return [
          { "value": "三全鲜食（北新泾店）", "address": "长宁区新渔路144号" },
          { "value": "Hot honey 首尔炸鸡（仙霞路）", "address": "上海市长宁区淞虹路661号" },
          ];
      },
      handleSelect(item) {
        console.log(item);
      }
    },
    mounted() {
      this.restaurants = this.loadAll();
    },
   watch: {
	},
	created(){
		//this.tabelData=new Array(this.pageSize);
		//this.getData(this.$route.query);
		//if(!this.loadcomplete)
		//	this.defaultdata();
		this.totalNum=this.tabelData.length;
    },   
}
</script>
<style>
    .el-tooltip__popper{max-width:40%}
</style>
<style scoped>
.apilist{
	position:relative;
	margin-top:30px;
	width:93%;
	left:3%;
}
.el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
}
.searchblock{
	left:35%;
	margin-top: 30px;
	position:relative;
	background-color:#E4E7ED;
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
  background-color:#E4E7ED;
  bottom:10px;
  left: 40%;
  position:fixed;
  z-index:1;
}
</style>