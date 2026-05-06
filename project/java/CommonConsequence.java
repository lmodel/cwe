package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Individual consequence associated with a weakness (CommonConsequencesType/Consequence in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CommonConsequence  {

  private String consequenceId;
  private List<String> scopes;
  private List<String> impacts;
  private String likelihood;
  private String note;

}