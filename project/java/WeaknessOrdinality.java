package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Potential ordering relationship with other weaknesses (WeaknessOrdinalitiesType/Weakness_Ordinality in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WeaknessOrdinality  {

  private String ordinality;
  private String description;

}