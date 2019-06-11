package class01;

public class Code05_BitMap {

	public static void main(String[] args) {

		int[] arr = new int[10]; // 32bit * 10 -> 320 bits

		int i = 178; // 请把178位的状态改成1

		arr[i / 32] = arr[i / 32] | (1 << (i % 32));

		i = 178; // 请把178位的状态改成0

		arr[i / 32] = arr[i / 32] & (~(1 << (i % 32)));

		i = 178; // 请把178位的状态拿出来

		// bit 0 1
		int bit = (arr[i / 32] >> (i % 32)) & 1;

	}

}
