# api usage case recommendation

一种API学习案例推荐服务，相比于其他API及代码推荐研究，其基于更大粒度的多函数功能模块进行API推荐研究。同时，没有通过单函数注释抽取代码功能描述，而是从监听请求入口，得到概括性语义特征。本仓库主要包括前后端实现，研究数据涉及仓库用户名等信息进行close处理，需要请联系仓库owner。
- 项目架构
![image](https://user-images.githubusercontent.com/46640542/200562061-bed1f652-6044-44cf-bdb5-8fb09651b8bf.png)
- 项目方法
  - 代码抽取
  选择Spring Boot框架实现的3 000个GitHub开源项目，识别监听接口注解代码行并抽取其中的URL命名，通过驼峰命名法切词并对特殊字符做额外处理，统计包含的动词描述。在得到的结果中，选择语义信息明确且拥有超过300个案例的动词作为选定使用场景，得到的七个使用场景分类如表2案例数量少于300的使用场景不能很好地满足后续分析筛选的需要。
  - 多函数片段融合
   ![image](https://user-images.githubusercontent.com/46640542/200562496-bf322cf8-dfd7-463e-b67d-3138d0449897.png)
   ![image](https://user-images.githubusercontent.com/46640542/200562523-2993f081-8bca-4ebc-882a-c4b68e8a282b.png)
  - 案例相似度评估与推荐
    - 图核算法（主要参考Gu X, Zhang H, Kim S. Codekernel: A graph kernel based approach to the selection of api usage examples[C]//2019 34th IEEE/ACM International Conference on Automated Software Engineering. IEEE, 2019: 590-601）
   
    - 谱聚类：将所有的数据都看作空间中的点，这些点之间可以用边连接起来，彼此之间的边的权值与点之间的距离正相关。通过对所有点组成的连接图进行切分子图工作，使得不同的子图之间的连边具有比较低的权值，而子图内的连边具有比较高的权值，从而达到聚类的目的。在本文已知相似度矩阵的情况下，使用谱聚类能够有效地得到结果。
- 前端实现：
   - vue.js
   - ![image](https://user-images.githubusercontent.com/46640542/200565127-e8c2d0eb-ba93-40df-b3ac-930db6211b10.png)

- 后端实现
   - flask
- 服务运行
   - npm install & npm run serve
   

  
