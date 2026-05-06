package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Information about how and when a weakness may be introduced (ModesOfIntroductionType/Introduction in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ModeOfIntroduction  {

  private String phase;
  private String note;

}