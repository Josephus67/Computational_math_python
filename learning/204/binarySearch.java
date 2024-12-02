/* 
public class binarySearch {
    public static void main(String[] args){
        int[] array={1,3,5,7,9};
        int target=11;
        int high=array.length+1;
        int low=0;
        float mid =(high+low)/2;
        int mid1=Math.round(mid);
        int mid2=Math.round((high+mid1)/2);
        int mid3=Math.round((high+mid2));
        if (target==array[mid1]){
            System.out.println(target+" can be found in the array index "+mid1);
        }
        else if (target>mid1){
            low=mid1;

        }
        if (target>mid2){}
    }
}
*/