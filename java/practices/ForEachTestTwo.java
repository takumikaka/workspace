public class ForEachTestTwo{
    public static void main(String[] args){
        String[] bookList = {"book1", "book2", "book3"};
        for(String book: bookList){
            book = "book3";
            System.out.println(book);
        }
        System.out.println(bookList[1]);
    }
}
