package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A target stakeholder group for a CWE view or category (AudienceType/Stakeholder in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Audience  {

  private String type;
  private String description;

}