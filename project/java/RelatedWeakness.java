package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Typed directional relationship from one CWE entry to another (RelatedWeaknessesType/Related_Weakness in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedWeakness  {

  private String nature;
  private int cweId;
  private int viewId;
  private Integer chainId;
  private String ordinal;

}