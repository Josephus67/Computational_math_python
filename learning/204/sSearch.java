public class sSearch {
    public static void main(String[] args){
        int[] array={1,2,2,5,8,9,90,3,23,43,54};
        int target=900;
        int i=0;
        while (i<array.length && array[i]!=target) {
            i++;
        }
        if (i<array.length){
            System.out.println(target+" can be found in index "+i);
        }
        else{
            System.out.println(-1);
        }
    }
    
}
