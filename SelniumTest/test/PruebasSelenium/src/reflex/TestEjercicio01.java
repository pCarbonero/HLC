package reflex;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestEjercicio01 {
	static WebDriver driver1;

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
	}

	@Test
	void test01() {
		driver1.get("http://localhost:3000/");
		WebElement textoAlto = driver1.findElement(By.id("enlacesFav"));

		assertEquals(textoAlto.getText(), "Enlaces favoritos");
	}
	
	@Test
	void test02() {
		driver1.get("http://localhost:3000/");
		WebElement enlace = driver1.findElement(By.id("linkBuscadores"));
		enlace.click();
		
		try {
			Thread.sleep(500);
		}catch(Exception e) {
			e.printStackTrace();
		}		
		
		String url = driver1.getCurrentUrl();
		assertEquals("http://localhost:3000/buscadores/", url);
	}
	
	@Test
	void test03() {
		driver1.get("http://localhost:3000/");
		WebElement enlace = driver1.findElement(By.id("linkRrss"));
		enlace.click();
		
		try {
			Thread.sleep(500);
		}catch(Exception e) {
			e.printStackTrace();
		}
				
		String url = driver1.getCurrentUrl();

		assertEquals("http://localhost:3000/redessociales/", url);
	}
	
	@Test
	void test04() {
		driver1.get("http://localhost:3000/buscadores/");
		WebElement titulo = driver1.findElement(By.id("tituloBuscadores"));

		assertEquals(titulo.getText(), "BUSCADORES");
	}
	
	@Test
	void test05() {
		driver1.get("http://localhost:3000/buscadores/");
		WebElement enlace = driver1.findElement(By.id("linkGoogle"));
		enlace.click();	
		
		ArrayList<String> tabs = new ArrayList<String> (driver1.getWindowHandles());
	    driver1.switchTo().window(tabs.get(1));
		
		String url = driver1.getCurrentUrl();
		driver1.close();
	    driver1.switchTo().window(tabs.get(0));
		assertEquals("https://www.google.com/", url);
	}
	
	@Test
	void test06() {
		driver1.get("http://localhost:3000/buscadores/");
		WebElement enlace = driver1.findElement(By.id("linkBing"));
		enlace.click();	
		
		ArrayList<String> tabs = new ArrayList<String> (driver1.getWindowHandles());
	    driver1.switchTo().window(tabs.get(1));
		
		String url = driver1.getCurrentUrl();

		driver1.close();
	    driver1.switchTo().window(tabs.get(0));
	    assertTrue(url.startsWith("https://www.bing.com"));
	}
	
	@Test
	void test07() {
			driver1.get("http://localhost:3000/buscadores/");
			WebElement enlace = driver1.findElement(By.id("linkBaidu"));
			enlace.click();	
			
			ArrayList<String> tabs = new ArrayList<String> (driver1.getWindowHandles());
		    driver1.switchTo().window(tabs.get(1));
		    
			String url = driver1.getCurrentUrl();
			
			driver1.close();
		    driver1.switchTo().window(tabs.get(0));
			assertEquals("https://www.baidu.com/", url);
	}
	
	@Test
	void test08() {
			driver1.get("http://localhost:3000/buscadores/");
			WebElement enlace = driver1.findElement(By.id("linkVolver"));
			enlace.click();	
			
			try {
				Thread.sleep(500);
			}catch(Exception e) {
				e.printStackTrace();
			}
		    
			String url = driver1.getCurrentUrl();

			assertEquals("http://localhost:3000/", url);
	}
	
	
	// refes sociale
	
	@Test
	void test09() {
		driver1.get("http://localhost:3000/redessociales/");
		WebElement enlace = driver1.findElement(By.id("ig"));
		enlace.click();	
		
		ArrayList<String> tabs = new ArrayList<String> (driver1.getWindowHandles());
	    driver1.switchTo().window(tabs.get(1));
		
		String url = driver1.getCurrentUrl();
		driver1.close();
	    driver1.switchTo().window(tabs.get(0));
		assertEquals("https://www.instagram.com/", url);
	}
	
	@Test
	void test10() {
		driver1.get("http://localhost:3000/redessociales/");
		WebElement enlace = driver1.findElement(By.id("tiktok"));
		enlace.click();	
		
		ArrayList<String> tabs = new ArrayList<String> (driver1.getWindowHandles());
	    driver1.switchTo().window(tabs.get(1));
		
		String url = driver1.getCurrentUrl();

		driver1.close();
	    driver1.switchTo().window(tabs.get(0));
	    assertTrue(url.startsWith("https://www.tiktok.com"));
	}
	
	@Test
	void test11() {
			driver1.get("http://localhost:3000/redessociales/");
			WebElement enlace = driver1.findElement(By.id("fb"));
			enlace.click();	
			
			ArrayList<String> tabs = new ArrayList<String> (driver1.getWindowHandles());
		    driver1.switchTo().window(tabs.get(1));
		    
			String url = driver1.getCurrentUrl();

			driver1.close();
		    driver1.switchTo().window(tabs.get(0));
			assertEquals("https://www.facebook.com/", url);
	}
	
	@Test
	void test12() {
			driver1.get("http://localhost:3000/redessociales/");
			WebElement enlace = driver1.findElement(By.id("linkVolverRs"));
			enlace.click();	
			
			try {
				Thread.sleep(500);
			}catch(Exception e) {
				e.printStackTrace();
			}
		    
			String url = driver1.getCurrentUrl();

			assertEquals("http://localhost:3000/", url);
	}

}
