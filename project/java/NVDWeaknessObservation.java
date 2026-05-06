package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Weakness observation from an NVD vulnerability detail page.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NVDWeaknessObservation  {

  private String observationId;
  private String observedInCve;
  private Weakness weakness;
  private String reportedBy;
  private String source;

}