import java.util.*;
class Greatest_Common_Divisor {
  public static void main(String args[]){
  //input
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    //output
        System.out.println(gcd(a,b));
  }
  //判定
  static int gcd(int x, int y){
    int tmp;

    if(x<y){
      tmp = x;
      x = y;
      y = tmp;
    }
    while(y>0){
      tmp = x%y;
      x = y;
      y = tmp;
    }
    return x;
  }
}