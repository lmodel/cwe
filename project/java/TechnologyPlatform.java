package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A technology or technology class applicable to a weakness (Technology element in ApplicablePlatformsType).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TechnologyPlatform  {

  private String name;
  private String class;
  private String prevalence;

}