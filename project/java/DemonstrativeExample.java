package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A code example illustrating how a weakness may appear (DemonstrativeExamplesType/Demonstrative_Example in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DemonstrativeExample  {

  private String demonstrativeExampleId;
  private String titleText;
  private String introText;
  private List<String> bodyTexts;
  private List<ExampleCode> exampleCodes;
  private List<CWEReference> references;

}