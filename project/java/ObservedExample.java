package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A reference to a real-world instance of a weakness, typically a CVE (ObservedExampleType/Observed_Example in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObservedExample  {

  private String reference;
  private String description;
  private String link;

}