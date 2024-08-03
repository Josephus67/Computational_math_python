public class uniqueness1 {
public static void main(String[] args){
    int[] array={2,3,4,6,5,8,9,12};
    int key=61;
    for (int i=0;i<array.length; i++){
        if (key==array[i]){
            System.out.println(key);
        }
    }
}    
}
