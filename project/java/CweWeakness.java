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
  A type of mistake or condition in software, firmware, hardware or a service that can leave a product open to attack.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweWeakness extends CweEntry {

  private String abstraction;
  private String structure;
  private String diagram;
  private String description;
  private String extendedDescription;
  private String technicalNuance;
  private List<CweDimension> dimensions;
  private List<CweRelatedWeakness> relatedWeaknesses;
  private List<CweWeaknessOrdinality> weaknessOrdinalities;
  private CweApplicablePlatforms applicablePlatforms;
  private List<String> backgroundDetails;
  private List<CweAlternateTerm> alternateTerms;
  private List<CweIntroduction> modesOfIntroduction;
  private List<String> exploitationFactors;
  private String likelihoodOfExploit;
  private List<CweConsequence> commonConsequences;
  private List<CweDetectionMethod> detectionMethods;
  private List<CweMitigation> potentialMitigations;
  private List<CweDemonstrativeExample> demonstrativeExamples;
  private List<CweObservedExample> observedExamples;
  private List<String> functionalAreas;
  private List<String> affectedResources;
  private List<CweTaxonomyMapping> taxonomyMappings;
  private List<CweRelatedAttackPattern> relatedAttackPatterns;


}