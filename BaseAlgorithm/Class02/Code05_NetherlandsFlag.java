package class02;
/*
荷兰国旗问题。因为荷兰国旗也是三个区域
功能：排序。快速排序的思想
partition思路: 当前值 带着 小于区域 和等于区域，向大于区域狂奔
将数组划分成  小于区域 + 等于区域 + 大于区域
从左向右遍历和划分值做对比。
1. 当前值 == 划分值。当前值向后移动一位。
2. 当前值 < 划分值。1)当前值和小于区域下一值交换。2)当前值向后移动一位。3)小于区域向右扩充一位（就是刚才的当前值位置）
3. 当前值 > 划分值。1)当前值和大于区域上一个值交换。2) 大于区域向左扩充一位。3) 当前值位置不变。
*/
public class Code05_NetherlandsFlag {

	public static int[] partition(int[] arr, int l, int r, int p) {
		// 小于区域 右边界
		int less = l - 1;
		// 大于区域 左边界
		int more = r + 1;
		// 当前值未 碰到大于区域
		while (l < more) {
			// 当前值 < 划分值
			if (arr[l] < p) {
				// 1) 交换当前值于小于区域后一个值。2) 小于区域向右扩充一位（就是刚才的当前值位置）3）当前值向后移动一位
				swap(arr, ++less, l++);
				// 当前值 > 划分值
			} else if (arr[l] > p) {
				swap(arr, --more, l);
				// 当前值 == 划分值
			} else {
				l++;
			}
		}
		// 返回等于区域 
		return new int[] { less + 1, more - 1 };
	}

	// for test
	public static void swap(int[] arr, int i, int j) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}

	// for test
	public static int[] generateArray() {
		int[] arr = new int[10];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (int) (Math.random() * 3);
		}
		return arr;
	}

	// for test
	public static void printArray(int[] arr) {
		if (arr == null) {
			return;
		}
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		int[] test = generateArray();

		printArray(test);
		int[] res = partition(test, 0, test.length - 1, 1);
		printArray(test);
		System.out.println(res[0]);
		System.out.println(res[1]);

	}
}
