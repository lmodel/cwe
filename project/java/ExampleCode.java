package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A structured code snippet within a demonstrative example (StructuredCodeType in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExampleCode  {

  private String nature;
  private String language;
  private String content;

}