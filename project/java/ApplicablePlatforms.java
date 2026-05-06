package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Languages, operating systems, architectures, and technologies where a weakness could appear (ApplicablePlatformsType in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ApplicablePlatforms  {

  private List<LanguagePlatform> languages;
  private List<OSPlatform> operatingSystems;
  private List<ArchitecturePlatform> architectures;
  private List<TechnologyPlatform> technologies;

}