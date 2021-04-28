<template>
    <div class="firstpage-wrap">
        <div class="bargainRecord_title">
            Springboot后端框架API学习案例推荐系统
        </div>
		<div class="interviewsmall">
            通过开源项目实例辅助学习
        </div>
		<el-card class="box-card" >
			<div class="interview">
				√常用API使用方法
			</div>
			<div class="interview">
				√常见使用场景实现过程
			</div>
			<div class="go" @click="ToDashboard">
				Click here to learn...
			</div>
		</el-card>
		
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            param: {
            },
            rules: {
            },
        };
    },
    methods: {
       ToDashboard(){
		this.$router.push("/dashboard");
	   }
    },
};
</script>

<style scoped>
.box-card {
	border-radius: 30px;
	border-width:3px;
    position: relative;
	top:55%;
	left:35%;
    width: 500px;
	background:rgba(0,0,0,0.5); 
　　opacity:0.2;

}
.go{
	font-family:"黑体";
	font-weight: 3px;
	font-size:x-large;
	left:2px;
    position: relative;
    color:#E6E6FA;
	top:55%
}
.interviewsmall{
	line-height:100%;
	font-family:"黑体";
	font-weight: 3px;
	font-size:42px;
    text-align: center;
    position: relative;
    color:#fff;
	top:47%
}
.interview{
	font-family:"黑体";
	font-weight: 2px;
	font-size:x-large;
	left:0px;
    position: relative;
    color:#E6E6FA;
	top:55%
}
.bargainRecord_title{
    font-weight: bold;
	font-size:50px;
    text-align: center;
    position: relative;
    color:#fff;
	top:40%
}
/*文字前*/
.bargainRecord_title:before {
    content: "";
    position: absolute;
     width: 10%;/*横线长度 */
    height: 3px;
    top: 50%;
    background: #fff;
    left: 10%;
  }
  /*文字后*/
.bargainRecord_title:after {
    content: "";
    position: absolute;
    width: 10%;
    height: 3px;
    top: 50%;
    background: #fff;
    right: 10%;
}
.firstpage-wrap {
    position: fixed;
    width:100%;
    height: 100%;
    background-size: 100%;
    background-repeat:no-repeat;
    background-attachment: fixed;
    background-image: url(../../assets/img/login5.png);
}
.head {
    width: 100%;
    height: 70px;
    background-color: #324157;
}
.head button {
    float: right;
    height: 36px;
    margin-left: 10px;
    margin-top: 15px;
}
.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 40px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}
.ms-firstpage {
    position: absolute;
    left: 30%;
    top: 30%;
    width: 1000px;
    margin: 190px 0 0 -175px;
    border-radius: 5px;
    overflow: hidden;
}
.ms-content {
    padding: 30px 30px;
}
.firstpage-btn {
    text-align: center;
}
.firstpage-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}
.firstpage-tips {
    font-size: 12px;
    line-height: 30px;
    color: #fff;
}
</style>