package class08;

public class Code06_ConvertToLetterString {

	public static int number(String str) {
		if (str == null || str.length() == 0) {
			return 0;
		}
		return process(str.toCharArray(), 0);
	}
    // i之前的位置，如何转化已经做过决定了，不用再关心
	// i之后的位置，有多少种可能进行统计。
	public static int process(char[] chs, int i) {
		// base case
		if (i == chs.length) {
			return 1;
		}
		// 下面都是 i 没有到终止为止的情况
		
		// 经过前面 i - 1 个转化，来到i位置，i位置为0的情况。此时没法转化
		if (chs[i] == '0') {
			return 0;
		}
		if (chs[i] == '1') {
			int res = process(chs, i + 1);
			if (i + 1 < chs.length) {
				res += process(chs, i + 2);
			}
			return res;
		}
		if (chs[i] == '2') {
			int res = process(chs, i + 1);
			if (i + 1 < chs.length && (chs[i + 1] >= '0' && chs[i + 1] <= '6')) {
				res += process(chs, i + 2);
			}
			return res;
		}
		return process(chs, i + 1);
	}

	public static void main(String[] args) {
		System.out.println(number("11111"));
	}

}
