# 图

遍历、最小生成树、最短路径、拓扑排序



# 遍历

BFS　＆　DFS： BFS依赖于队列，DFS　栈。后者可以用函数栈形式快速地实现

## BFS

```c
void BFSTraverse(Graph G)
{
	for(int i=0; i<G.vexnum; i++)
		visited[i] = FALSE;
	InitQueue(Q);
	for(i = 0; i< G.vexnum; i++)
		if(!visited[i])
			BFS(G, i)
}

void BFS(Graph G, int v)
{
	visit(v);
	visited[v] = TRUE;
	Enqueue(Q, v);
	while(!isEmpty(Q)){
		DeQueue(Q, v);
		for(w = FirstNeighbor(G, v); w>=0; w = NextNeighbor(G, v, w))
			if(!visited[w]){
				visit(w);
				visited[w]=TRUE;
				Enqueue(Q, w);
			}
	}//while
}
```

## DFS

```C
void DFSTraverse(Graph G)
{// 对图G进行深度优先遍历，访问函数为visit()
	for(v = 0; v < G.vexnum; ++v)
		visited[v] = FALSE;
	for(v = 0; v < G.vexnum; ++v)
		if(!visited[v])
			DFS(G, v)
}
void DFS(Graph G, v)
{//从 节点v 出发 递归遍历整个图
	visit(v);
	visited[v] = True;//访问 v 并置访问标志

	for(w = FirstNeighbor(G, u); w>=0; w = NextNeighbor(G, v, W))
		if(!visited[W])
			DFS(G, w)
		//if
}
```



* 迭代形式

```python
def DFSTraverse(G):
    visited = [False] * G.vetnum
    for v in G.vertices:
        if not visted[v]:
			dfs(G, v, visited)
def dfs(G, v, visited):
    stack = [v]
    while stack:
        v = stack.pop()
        visted[v] = True
        
        for nv in v.neighbours:
            if not visted[nv]:
                stack.push(nv)
```



# 最小生成树MST

一个连通图的生成树是图的极小连通子图。

对带权连通无向图G，其所有生成树中边权值和最小的树为最小生成树。

1. MST不唯一
2. MST权值和唯一
3. MST的边数为顶点数减一

构造MST的算法大多用了如下性质：设U为G.V的非空子集，若(u,v)是一条具有最小权值的边，其中u∈U,v∈V，则必存在一颗包含(u, v)的MST

```
Generic_MST(G){
    T = NULL;
    while T 不是一颗生成树:
    	找到一条具有最小代价边(u, v)并且在T中不形成回路
    		T = T∪(u, v);
}
```

## 普利姆算法Prim

从 某点v 开始依次加入节点 构成最小生成树 (该节点应能够使得未加入树的节点到树的距离最小)

```c
void Prim(G, T)
{
	T = 空集;			//初始化空树								
	U = {w};			//添加一个任意初始顶点
	while((V-U) != 空集){//当还有节点未加入树
		(u,v) = argmin(weight(u, v))  s.t u∈U, v∈V-U;
		T = T ∪ {(u, v)};
		U = U ∪ {v};
	}
}
```

## 克鲁斯卡尔算法 kruskal

对边按权值从小到大依次加入到生成树中 (该边应使树中无回路

```c
void Kruskal(V, T)
{
	T = V;				//初始化树 T, 仅含定点
	numS = n;			//不连通分量数
	while(numS > 1){	//当不连通的分量数目大于 1
		从 E 中取出权值最小的边(v, u);
		if(v u 属于两个不同的连通分量){ //当不形成回路时将边加入MST
			T = T∪ {(u, v)}；
			numS --;
		}
	}
}
```

## 总结

两种算法的适用场景

# 最短路径

## Dijkstra单源最短

Dijkstra  //v到某节点w距离最小的路径必然也是v到该路径上其他节点的最短路径
	a.找出距离源点v距离最小的邻接点w, 就找到从v到w的距离最小的路径.
	b.更新其他节点到源点v的距离.
	c.repeat a,b 直至找到v到所有节点的最短距离

```

```



## Floyd各顶点间最短

基本思想是递推产生一个序列 A...(-1 -> n-1) 每次只考虑一个节点





# 拓扑排序

1. DAG
2. 拓扑排序：图论中由一个DAG的顶点序列满足如下条件
   1. 每个顶点出现且只出现一次
   2. 若A在B前面，则在图中不存在从顶点B到A的路径
3. 拓扑排序算法
   1. 从DAG中选择一个入度为0的点v，输出
   2. 移除所有从v射出的边
   3. 重复1、2直到无剩余的顶点。（若存在剩余的顶点，则存在环，该图不为DAG）