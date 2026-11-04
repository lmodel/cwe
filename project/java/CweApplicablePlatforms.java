package example;

/* metamodel_version: 1.12.0 */
/* version: 5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The kinds of platform where a weakness can appear.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweApplicablePlatforms  {

  private List<CweLanguagePlatform> language;
  private List<CweOperatingSystemPlatform> operatingSystem;
  private List<CweArchitecturePlatform> architecture;
  private List<CweTechnologyPlatform> technology;


}