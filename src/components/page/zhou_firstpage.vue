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
      <div class="title">
        开源软件社区(GitHub)学习门户
      </div> 
      <div class="subtitle">
        开始搜索...
      </div>
      <div class="cards">
        <el-row>      
          <el-col :span="5" v-for="(item) in cases" :key="item.title" :offset="1" >               
              <el-card :body-style="{ padding: '1px'}" shadow="hover" style="background-color:#FFFFF0;height:">                    
                <div class="cardpiece" >                    
                  <div class="cardtitle" style="text-align:center;font-size:30px;font-family:Lucida Handwriting;margin-top:3%">
                    {{item.title}}
                  </div>
                  <div class="discription" style="margin-left:2%;margin-right:2%;margin-top:5%;font-size:25px;word-break:break-all;font-family:Georgia">
                    {{item.content}}
                  </div>  
                  <div class="detail" style="margin-left:2%;margin-right:2%;margin-top:5%;font-size:25px;word-break:break-all;font-family:Georgia">
                    detail:{{item.child}}
                  </div>        
                </div>                
              </el-card>            
            </el-col>   
        </el-row>
      </div>
      <el-button type="info" class="changeBun">
        换一批...
      </el-button>
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
      cases:[
        {
          title:' Web Development',
          icon:'el-icon-user',
          exist:false,
          content:` xxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  

           `,
          child:'click for detail'
        },
        {
          title:' Web Design',
          icon:'el-icon-s-fold',
          exist:true,
          content:` xxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  

           `,
          child:'click for detail'
        },
        {
          title:' Web Analytics',
          icon:'el-icon-s-unfold',
          exist:true,
          content:` xxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  

           `,
          child:'click for detail'
        }
      ]
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
</style>
