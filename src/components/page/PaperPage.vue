
<template>
<div class="mainpageblock">
<div class="pics">
  <template>
  <el-carousel :interval="4000" type="card" height="800px">
    <el-carousel-item v-for="item in pics" :key="item.url">
        <img :src="item.url"/>
      </el-carousel-item>
  </el-carousel>
</template>
</div>
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
			pics: [
        { url: require("../common/1.jpg") },
        {url: require("../common/2.jpg") },
        { url: require("../common/3.jpg") }
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
     
	},
	methods: {
	
	}
}
</script>

<style>
.pics{
  margin-top:3%;
}
 .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
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

/* optional */
.prism-editor__textarea:focus {
 outline: none;
}
 
/* not required: */
.height-300 {
 height: 300px;
}
</style>
