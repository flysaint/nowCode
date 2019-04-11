package class07;

import java.util.Arrays;
import java.util.Comparator;

public class Code04_BestArrange {

	public static class Program {
		public int start;
		public int end;

		public Program(int start, int end) {
			this.start = start;
			this.end = end;
		}
	}

	public static class ProgramComparator implements Comparator<Program> {

		@Override
		public int compare(Program o1, Program o2) {
			return o1.end - o2.end;
		}

	}

	public static int bestArrange(Program[] programs, int start) {
		// 多些几种对数器，方法一个一个试。找到最优解
		Arrays.sort(programs, new ProgramComparator());
		int result = 0;
		// 遍历项目
		for (int i = 0; i < programs.length; i++) {
			// 如果本次项目的时间 要晚于起始时间，则进行安排
			if (start <= programs[i].start) {
				// 安排的场次 ++
				result++;
				// 时间点来到项目的末尾
				start = programs[i].end;
			}
		}
		return result;
	}

	public static void main(String[] args) {

	}

}
