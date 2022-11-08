<template>
  <div>
    <div class="header">
      <div class="home-btn" @click="homeScreenChange">
        <i class="el-icon-s-home"></i>
      </div>    
      <div class="selectText">
        主页
      </div>
      <div class="nonselectText">
        帮助
      </div>
      <div class="nonselectText">
        关于我们
      </div>
    </div>

    <div class="content">
      <el-row :gutter="22">
        <el-col :span="11">
          <div class="png">
               <img :src="imgUrl"/>         
          </div>
          <el-button type="info" class="imgtitle" plain>
               返回父节点       
          </el-button>
          <div class="owncode" v-infinite-scroll="load" >
              <div style="font-size:15px;white-space:pre-wrap;"></div>
              <pre  class="language-java line-numbers">
      
              </pre>
          </div>
        </el-col>
        <el-col :span="11">
          <div class="information">
            <el-col :span="4">
              <div class="pngsub">
               <img :src="imgUrl2"/>         
              </div>
            </el-col>
            
              <div class="detailedInfo">
               个人简介：xxxxxxxxxxxxxx       
              </div>
              <div class="githublink">
               GitHub链接：https://github.com/graphdml-uiuc-jlu     
              </div>
          </div>

          <div class="dirlist">     
            <div class="firstline"> &nbsp;&nbsp; > &nbsp;&nbsp;实践配合仓库</div>
            <div class="secondline">{{listdata1}}</div>
            <div class="secondline">{{listdata2}}</div>
            <div class="secondline">{{listdata3}}</div>
            <div class="thirdline"> &nbsp;&nbsp;>&nbsp;&nbsp;相似依赖仓库</div>
            <div class="fourthline"> &nbsp;&nbsp;>&nbsp;&nbsp;相似知识点</div>
          </div>

    </el-col>
</el-row> 
    </div>  
  </div>
</template>
<script>
import bus from "../common/bus";
export default {
  data() {
    return {
      collapse: false,
      fullscreen: false,
      name: "linxin",
      message: 2,
      listdata1:" >> 1. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx "   ,     
           listdata2:" >> 2. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ",        
           listdata3:" >> 3. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx " ,      
      imgUrl:require("./web2.png"),
      imgUrl2:require("./photo.png"),
      dirs: [{
          label: '实践配合仓库',
          children: [{
            label: '二级 1-1',
            children: [{
              label: '三级 1-1-1'
            }]
          }]
        }, {
          label: '相似依赖仓库',
          children: [{
            label: '二级 2-1',
            children: [{
              label: '三级 2-1-1'
            }]
          }, {
            label: '二级 2-2',
            children: [{
              label: '三级 2-2-1'
            }]
          }]
        }, {
          label: '相似知识点',
          children: [{
            label: '二级 3-1',
            children: [{
              label: '三级 3-1-1'
            }]
          }, {
            label: '二级 3-2',
            children: [{
              label: '三级 3-2-1'
            }]
          }]
        }],
        defaultProps: {
          children: 'children',
          label: 'label'
        }
      };
  },
  computed: {
    username() {
    }
  },
  created() {
  },
  methods: {
  },
  mounted() {
    if (document.body.clientWidth < 1500) {
      this.collapseChage();
    }
  }
};
</script>
<style scoped>
.header {
  background-color: #A9A9A9;
  box-sizing: border-box;
  height: 8%;
  position: fixed;
  top: 0px;
  width: 100%;
  font-size: 22px;
  color: #fff;
  z-index: 50;
  border-style: outset;
}
.home-btn {
  margin-left:2%;
  float: left;
  padding: 0 5px;
  cursor: pointer;
  line-height: 70px;
  font-size: 30px;
}
.selectText{  
  margin-left:2%;
  float: left;
  padding: 0 5px;
  cursor: pointer;
  line-height: 70px;
  font-size: 20px;
  color: #FFFFF0;
}
.nonselectText{  
  margin-left:2%;
  float: left;
  padding: 0 5px;
  cursor: pointer;
  line-height: 70px;
  font-size: 20px;
  color: #DCDCDC;
}
.content{
  background-color:#DCDCDC;
  box-sizing: border-box;
  height:100%;
  position: fixed;
  top: 8%;
  width: 100%;
  font-size: 22px;
  color: #fff;
  z-index: 50;
}
.title{
  margin-left:29%;
  margin-right:40%;
  position: fixed;
  top: 27%;
  width: 100%;
  font-size: 60px;
  color: #696969;
  z-index: 50;
  font-family:"Times New Roman";
}
.subtitle{
  margin-left:45%;
  margin-right:40%;
  position: fixed;
  top: 40%;
  width: 100%;
  font-size: 40px;
  color: #778899;
  z-index: 50;
  font-family:"Times New Roman";
}
.cards{  
  margin-left:10%;
  margin-right:10%;
  position: fixed;
  top: 50%;
  width: 100%;
  z-index: 50;
}
.changeBun{  
  margin-left:46%;
  margin-right:40%;
  width:10%;
  position: fixed;
  font-size: 30px;
  top: 85%;
  z-index: 50;
  color: #FFFFF0;
  font-family:"Times New Roman";
  background-color: #A9A9A9;
}
.png{  
  margin-left:5%;
  margin-right:50%;
  width:100%;
  position: fixed;
  font-size: 30px;
  top: 20%;
  z-index: 50;
}
.imgtitle{  
  margin-left:13%;
  margin-right:75%;
  position: fixed;
  top: 85%;
  font-size: 25px;
  color: #778899;
  z-index: 50;
  font-family:"Times New Roman";
}
.dirlist{  
  margin-left:3%;
  margin-right:3%;
  position: fixed;
  top: 60%;
  font-size: 20px;
  color: #FFFFF0;
  z-index: 50;
  font-family:"Times New Roman";
  height: 100%;
  width:45%;
}
.firstline {
  width: 100%;
  float: right;
  font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
  font-size: 20px;
  color: #000000;
  background-color: #C0C0C0;
  line-height: 35px;
  letter-spacing: 1px;
  padding:5px;
  border-style: double;
}
.secondline {
  width: 100%;
  height:30px;
  float: right;
  font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
  font-size: 15px;
  color:  #808080;
  background-color:#D3D3D3;
  padding:5px;
  text-align:center;
  line-height: 30px;
  letter-spacing: 1px;
  border-bottom: double;
  border-left:double;
  border-right:double;
}
.thirdline {
  width: 100%;
  float: right;
  font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
  font-size:  20px;
  color:  #000000;
  background-color: #C0C0C0;
  line-height: 35px;
  letter-spacing: 1px;
  padding:5px;
  border-bottom: double;
  border-left:double;
  border-right:double;
}
.fourthline {
  width: 100%;
  float: right;
  font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
  font-size:  20px;
  color:  #000000;
  background-color: #C0C0C0;
  line-height: 35px;
  letter-spacing: 1px;
  padding:5px;
  border-bottom: double;
  border-left:double;
  border-right:double;
}
.information{
  margin-left:3%;
  margin-right:3%;
  position: fixed;
  top: 15%;
  width:40%;
  height:30%;
  float: right;
  font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
  font-size:  20px;
}
.pngsub{
  margin-left:3%;
  margin-right:3%;
  margin-top:10%;

}
.detailedInfo{
  margin-left:40%;
  margin-right:3%;
  margin-top:10%;
  font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
  font-size:  25px;
  color:  #778899;
  font-weight:bold;
}
.githublink{
  margin-top:25%;
  font-family: “Times New Roman”, Arial, Helvetica, sans-serif;
  font-size:  23px;
  color:  #808080;
  font-weight:bold;
  z-index: 50;
  text-align:center;
}
</style>
