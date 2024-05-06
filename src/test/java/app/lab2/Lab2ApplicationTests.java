package app.lab2;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.client.RestTemplate;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class Lab2ApplicationTests {
	
	@Test
	@CrossOrigin(origins = "http://localhost:3000")
	void successTest() {
		String a = "0";
		String b = "1.5";
		String gNum = "0";
		String mNum = "0";
		String error = "0.01";
		String answer = "None";
		String filepath = "";
		
		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
		
		MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
		map.add("lbname", "value");
		map.add("type", "true");
		map.add("quation", gNum);
		map.add("method", mNum);
		map.add("leftBorder", a);
		map.add("rightBorder", b);
		map.add("inaccuary", error);
		map.add("answer", answer);
		map.add("filepath", filepath);
		
		HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);
		
		String url = "http://localhost:8080/api/run-python-script";
		
		RestTemplate restTemplate = new RestTemplate();
		
		String response = restTemplate.exchange(url, HttpMethod.POST, entity, String.class).getBody();
		assertEquals("1.92", response, "");
	}
	
	@Test
	@CrossOrigin(origins = "http://localhost:3000")
	void wrongTest() {
		String a = "";
		String b = "1.5";
		String gNum = "0";
		String mNum = "0";
		String error = "0.01";
		String answer = "None";
		String filepath = "";
		
		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
		
		MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
		map.add("lbname", "value");
		map.add("type", "true");
		map.add("quation", gNum);
		map.add("method", mNum);
		map.add("leftBorder", a);
		map.add("rightBorder", b);
		map.add("inaccuary", error);
		map.add("answer", answer);
		map.add("filepath", filepath);
		
		HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);
		
		String url = "http://localhost:8080/api/run-python-script";
		
		RestTemplate restTemplate = new RestTemplate();
		
		String response = restTemplate.exchange(url, HttpMethod.POST, entity, String.class).getBody();
		assertNull(response);
	}
}