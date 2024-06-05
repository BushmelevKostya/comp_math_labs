package app.lab2;

import java.lang.reflect.Array;
import java.util.List;
import java.util.Map;

public record SubmitRequest(List<Float> floatValues, Integer intValue, String selectedFunc) {}
