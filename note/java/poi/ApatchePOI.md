# Apache POI
[Apache POI](https://poi.apache.org/)
## 学习来由
因为在定位公司的OOM的时候，没完全定位问题，后来海琪定位出是因为POI中的使用表格对象原因：
> 当数据量超出65536条后，在使用HSSFWorkbook或XSSFWorkbook，程序会报OutOfMemoryError：Javaheap space;内存溢出错误。这时应该用SXSSFworkbook。

嗯，没错我啥也不知道，只是知道POI是一个文件OI的工具，具体啥干啥就不知道了。
所以问题解决的第一天特意学习一下。

## Why should I use Apache POI?
A major use of the Apache POI api is for Text Extraction applications such as web spiders, index builders, and content management systems.

So why should you use POIFS, HSSF or XSSF?

You'd use POIFS if you had a document written in OLE 2 Compound Document Format, probably written using MFC, that you needed to read in Java. Alternatively, you'd use POIFS to write OLE 2 Compound Document Format if you needed to inter-operate with software running on the Windows platform. We are not just bragging when we say that POIFS is the most complete and correct implementation of this file format to date!

You'd use HSSF if you needed to read or write an Excel file using Java (XLS). You'd use XSSF if you need to read or write an OOXML Excel file using Java (XLSX). The combined SS interface allows you to easily read and write all kinds of Excel files (XLS and XLSX) using Java. Additionally there is a specialized SXSSF implementation which allows to write very large Excel (XLSX) files in a memory optimized way.

> OLE: (Object Linkingand Embedding)对象链接和嵌入
>
> MFC:(Microsoft Foundation Classes)微软基础类库
>
> OOXML: (Office Open XML standards)微软公司为Office 2007产品开发的技术规范，现已成为国际文档格式标准，兼容前国际标准开放文档格式和中国文档标准“标文通”（外语简称：UOF）。
>
> Excel workbooks (SS=HSSF+XSSF)

POI工具用于文档提取应用，如：网页爬虫，索引构建，系统管理。

使用Java进行OLE2格式的读写使用POIFS。

使用Java读写.xls格式的Excel表格使用HSSF，读写.xlsx格式Excel表格使用XSSF，SS就可以同时处理两种格式的Excel表格。
另外，大量数据的导出使用优化过的SXSSF。

## 测试代码
```` java
package my.poi;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class XSSF {

    public static void main(String[] args) throws IOException, InterruptedException {
        // Thread.sleep(3 * 1000);  这个是为了能够使用监控到内存的使用
        (new XSSF()).generateXLSX(8, 5000, 500);
    }

    public void generateXLSX(int sheetNum, int rowNum, int column) {
        String fileName = FILE_PATH + FILE_NAME_PREFIX + (rowNum * sheetNum) + SEPARATOR + new Random().nextLong() + FILE_NAME_SUFFIX;
        OutputStream out = new FileOutputStream(fileName);
        Workbook workbook = generateSheet(sheetNum, rowNum, column);
        workbook.write(out);
        workbook.close();
        out.close();
    }

    private Workbook generateSheet(int sheetNum, int rowNum, int column) throws IOException {
        Workbook workbook = new XSSFWorkbook();  //其实就是就是new一个对象的问题@_@
        for (int sheetIndex = 0; sheetIndex < sheetNum; sheetIndex++) {
            String sheetName = SHEET_NAME_PREFIX + SEPARATOR + sheetIndex;
            Sheet sheet = workbook.createSheet(sheetName);
            for (int i = 0; i < rowNum; i++) {
                Row row = sheet.createRow(i);
                for (int j = 0; j < column; j++) {
                    Cell cell = row.createCell(j);
                    cell.setCellValue(sheetName + "-" + i + "-" + j);
                }
            }
        }
        return workbook;
    }
}


package my.poi;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class SXSSF {

    public static void main(String[] args) throws IOException, InterruptedException {
        // Thread.sleep(3 * 1000);  这个是为了能够使用监控到内存的使用
        (new XSSF()).generateXLSX(8, 5000, 500);
    }

    public void generateXLSX(int sheetNum, int rowNum, int column) {
        String fileName = FILE_PATH + FILE_NAME_PREFIX + (rowNum * sheetNum) + SEPARATOR + new Random().nextLong() + FILE_NAME_SUFFIX;
        OutputStream out = new FileOutputStream(fileName);
        Workbook workbook = generateSheet(sheetNum, rowNum, column);
        workbook.write(out);
        workbook.close();
        out.close();
    }

    private Workbook generateSheet(int sheetNum, int rowNum, int column) throws IOException {
        Workbook workbook = new SXSSFWorkbook();  //其实就是就是new一个对象的问题@_@
        for (int sheetIndex = 0; sheetIndex < sheetNum; sheetIndex++) {
            String sheetName = SHEET_NAME_PREFIX + SEPARATOR + sheetIndex;
            Sheet sheet = workbook.createSheet(sheetName);
            for (int i = 0; i < rowNum; i++) {
                Row row = sheet.createRow(i);
                for (int j = 0; j < column; j++) {
                    Cell cell = row.createCell(j);
                    cell.setCellValue(sheetName + "-" + i + "-" + j);
                }
            }
        }
        return workbook;
    }
}

````
Maven依赖的jar包
```xml
  <!-- https://mvnrepository.com/artifact/org.apache.poi/poi -->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi</artifactId>
            <version>${poi.version}</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml -->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-ooxml</artifactId>
            <version>3.11</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml-schemas -->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-ooxml-schemas</artifactId>
            <version>3.11</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.poi/poi-scratchpad -->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-scratchpad</artifactId>
            <version>3.11</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.apache.poi/poi-excelant -->
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-excelant</artifactId>
            <version>3.11</version>
        </dependency>
```







