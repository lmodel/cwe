package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A processor architecture or class applicable to a weakness (Architecture element in ApplicablePlatformsType).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArchitecturePlatform  {

  private String name;
  private String class;
  private String prevalence;

}