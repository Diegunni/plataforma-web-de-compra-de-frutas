package mx.uam.integracion;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Main {

    public static void main(String[] args) throws Exception {

        HttpClient client = HttpClient.newHttpClient();

        String frutaJson = "{\"id\":1,\"nombre\":\"Manzana\",\"precio\":25}";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://localhost:8000/frutas"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(frutaJson))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Respuesta del servidor:");
        System.out.println(response.body());
    }
}
