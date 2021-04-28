<template>
<div>
<el-row :gutter="20">
<el-breadcrumb separator-class="el-icon-arrow-right" style="font-size:20px;left:20px;position:absolute">
	  <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
	  <el-breadcrumb-item>帮助</el-breadcrumb-item>
	</el-breadcrumb>
<el-col :span="24">	
	
</el-col>
</el-row>	
</div>
</template>
<script>
  export default {
    data() {
      return {
        activeNames: ['1']
      };
    },
    methods: {
      handleChange(val) {
        console.log(val);
      }
    }
  }
</script>
<style scoped>

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

</style>