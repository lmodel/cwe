package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Another name by which this weakness may be known (AlternateTermsType/Alternate_Term in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlternateTerm  {

  private String term;
  private String description;

}