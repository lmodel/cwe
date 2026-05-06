package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A method that may be employed to detect a weakness, with effectiveness (DetectionMethodsType/Detection_Method in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DetectionMethod  {

  private String detectionMethodId;
  private String method;
  private String description;
  private String effectiveness;
  private String effectivenessNotes;

}