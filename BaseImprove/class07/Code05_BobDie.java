package class07;

public class Code05_BobDie {

	public static String bob1(int N, int M, int i, int j, int K) {
		long all = (long) Math.pow(4, K);
		long live = process(N, M, i, j, K);
		long gcd = gcd(all, live);
		return String.valueOf((live / gcd) + "/" + (all / gcd));
	}

	// M*N的区域，Bob在(row,col)位置，走rest步之后，获得生存点数
	// 即是 活着的走法。总共有几种走法，4^K。因为每次有4个方向，走k步，因此是4^k步。
	// 动态规划怎么改？rest == 0 的时候是已知的，从rest ==0 往上推。
	public static long process(int N, int M, int row, int col, int rest) {
		if (row < 0 || row == N || col < 0 || col == M) {
			return 0;
		}
		// row,col 没越界
		if (rest == 0) {
			return 1;
		}
		// 还没走完，row,col也没越界
		long live = process(N, M, row - 1, col, rest - 1);
		live += process(N, M, row + 1, col, rest - 1);
		live += process(N, M, row, col - 1, rest - 1);
		live += process(N, M, row, col + 1, rest - 1);
		return live;
	}

	public static long gcd(long m, long n) {
		return n == 0 ? m : gcd(n, m % n);
	}

	public static String bob2(int N, int M, int i, int j, int K) {
		int[][][] dp = new int[N + 2][M + 2][K + 1];
		for (int row = 1; row <= N; row++) {
			for (int col = 1; col <= M; col++) {
				dp[row][col][0] = 1;
			}
		}
		for (int rest = 1; rest <= K; rest++) {
			for (int row = 1; row <= N; row++) {
				for (int col = 1; col <= M; col++) {
					dp[row][col][rest] = dp[row - 1][col][rest - 1];
					dp[row][col][rest] += dp[row + 1][col][rest - 1];
					dp[row][col][rest] += dp[row][col - 1][rest - 1];
					dp[row][col][rest] += dp[row][col + 1][rest - 1];
				}
			}
		}
		long all = (long) Math.pow(4, K);
		long live = dp[i + 1][j + 1][K];
		long gcd = gcd(all, live);
		return String.valueOf((live / gcd) + "/" + (all / gcd));
	}

	public static void main(String[] args) {
		int N = 10;
		int M = 10;
		int i = 3;
		int j = 2;
		int K = 5;
		System.out.println(bob1(N, M, i, j, K));
		System.out.println(bob2(N, M, i, j, K));
	}

}
