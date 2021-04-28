<template>
<div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            background-color="#606266"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="item in items">                
                <template>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
		
    </div>
</template>

<script>
import bus from '../common/bus';
export default {
    data() {
        return {
            collapse: true,
            items: [
				{
                    icon: 'el-icon-s-home',
                    index: 'firstpage',
                    title: '返回主页',
                },
                {
                    icon: 'el-icon-search',
                    index: 'dashboard',
                    title: '通过单个API查找相应使用场景实现',
                },
                {
                    icon: 'el-icon-s-order',
                    index: 'case',
                    title: '常用后端场景案例学习',
                },
				{
                    icon: 'el-icon-question',
                    index: 'help',
                    title: '帮助',
                }
            ]
        };
    },
	methods: {
		/*
		search_cat(e){
			//console.log(e.target);
			//console.log(e.currentTarget.getElementById("string"));
			console(e);
			var category=e;
				
		},		
		*/
	},
    computed: {
        onRoutes() {
			/*
			var url=this.$url;
			var k=0;
			var L=url.length;
			while(k<L)
			{
				if (url[k]=='#')
				{
					k++;
					break;
				}
			}
			url=url.substring(0,k);
            return url;
			*/
			var pre=this.$route.path.replace('/','');
			//console.log(pre);
			return pre;
        }
    },
    created() {
        // 通过 Event Bus 进行组件间通信，来折叠侧边栏
        bus.$on('collapse', msg => {
            this.collapse = msg;
            bus.$emit('collapse-content', msg);
        });
    }
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 0px;
    bottom: 0;
    overflow-y: scroll;
    z-index:50;
    float: left;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 350px;
}
.sidebar > ul {
    height: 100%;
}
</style>