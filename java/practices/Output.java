public interface Output{
    int MAX_CACHE_LINE = 50;
    void out();
    void getData(String msg);
    void print(String... msgs);
}
