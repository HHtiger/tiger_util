import java.io.File;
import java.net.URL;

/**
 * Package: com.founder.utils
 * ClassName: ClassPathUtil
 * Author: he_hu@founder.com.cn
 * Description:根据当前工具类定位项目路径。用户tomcat，webspere等不同环境的项目根路径获取。
 * CreateDate: 2016/3/15
 * Version: 1.0
 */
public class ClassPathUtil {
    /**
     * 取得当前类所在的文件
     * @param clazz
     * @return
     */
    public static File getClassFile(Class clazz){
        URL path = clazz.getResource(clazz.getName().substring(
                clazz.getName().lastIndexOf(".")+1)+".classs");
        if(path == null){
            String name = clazz.getName().replaceAll("[.]", "/");
            path = clazz.getResource("/"+name+".class");
        }
        return new File(path.getFile());
    }
    /**
     * 得到当前类的路径
     * @param clazz
     * @return
     */
    public static String getClassFilePath(Class clazz){
        try{
            return java.net.URLDecoder.decode(getClassFile(clazz).getAbsolutePath(),"UTF-8");
        }catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            return "";
        }
    }

    /**
     * 取得当前类所在的ClassPath目录，比如tomcat下的classes路径
     * @param clazz
     * @return
     */
    public static File getClassPathFile(Class clazz){
        File file = getClassFile(clazz);
        for(int i=0,count = clazz.getName().split("[.]").length; i<count; i++)
            file = file.getParentFile();
        if(file.getName().toUpperCase().endsWith(".JAR!")){
            file = file.getParentFile();
        }
        return file;
    }
    /**
     * 取得当前类所在的ClassPath路径
     * @param clazz
     * @return
     */
    public static String getClassPath(Class clazz){
        try{
            return java.net.URLDecoder.decode(getClassPathFile(clazz).getAbsolutePath(),"UTF-8");
        }catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            return "";
        }
    }

    public static void main(String[] args){
        String webRootPath = getClassFilePath(ClassPathUtil.class).replace("\\","/");
        System.out.println(webRootPath);
        webRootPath = webRootPath.substring(0,webRootPath.lastIndexOf("/WEB-INF"));
        System.out.println(getClassPath(UrlUtil.class));
    }

}