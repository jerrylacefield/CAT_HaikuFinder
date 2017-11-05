package manager;

public class Request {

    /**
     * 
     */
    private final String link;
    /**
     * 
     */
    private final int type;
    /**
     * 
     */
    private final String data[];

    public Request(long id, String link, int type, String data[]) {
        this.link = link;
        this.type = type;
        this.data = data;
    }

    public int getType() {
        return type;
    }

    public String[] getData() {
        return data;
    }

    public String getLink() {
        return link;
    }
}
