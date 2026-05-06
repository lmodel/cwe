package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  An operating system or OS class applicable to a weakness (Operating_System element in ApplicablePlatformsType).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OSPlatform  {

  private String name;
  private String class;
  private String version;
  private String cpeId;
  private String prevalence;

}