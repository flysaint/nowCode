package class02;

import java.util.PriorityQueue;

/*
问题。一个连续k位都有序的数组
已知一个几乎有序的数组，几乎有序是指，如果把数组排好顺序的话，每个元
素移动的距离可以不超过k，并且k相对于数组来说比较小。请选择一个合适的
排序算法针对这个数据进行排序。

思路：
依此把下一个数放小根堆，再放到该去的位置
*/
public class Code04_SortArrayDistanceLessK {

	public void sortedArrDistanceLessK(int[] arr, int k) {
		// 默认是小顶堆
		PriorityQueue<Integer> heap = new PriorityQueue<>();
		int index = 0;
		// 数据插入堆，在不超过数组长度和k的情况下
		for (; index < Math.min(arr.length, k); index++) {
			heap.add(arr[index]);
		}
		// 将数组剩余值入栈；依此入栈，出栈到数组中
		int i = 0;
		for (; index < arr.length; i++, index++) {
			heap.add(arr[index]);
			arr[i] = heap.poll();
		}
		// 依此出栈
		while (!heap.isEmpty()) {
			arr[i++] = heap.poll();
		}
	}
}
