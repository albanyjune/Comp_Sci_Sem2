import java.util.Scanner;


class starter {
	public static void main(String args[]) {
		// the string "I love to learn coding remotely." will appear in
		// the command window when you compile and run this program.
		Scanner sc = new Scanner(System.in);
		int f = sc.nextInt();
		sc.nextLine();
		int count = 0;
		while (count!=f){
			System.out.println(f+1);
			if (count==5){
				break;
			}
			count = count + 1;
		}
			
		
		
	}
}
