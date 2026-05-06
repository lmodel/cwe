package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A potential mitigation for a weakness (PotentialMitigationsType/Mitigation in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PotentialMitigation  {

  private String mitigationId;
  private List<String> phases;
  private String strategy;
  private String description;
  private String effectiveness;
  private String effectivenessNotes;

}